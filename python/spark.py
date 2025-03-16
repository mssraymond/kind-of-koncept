from pyspark.sql import SparkSession


def spark_streaming(host, topic, port):
    scala_version = "2.12"
    spark_version = "3.5.5"
    kafka_version = "3.1.0"
    packages = [
        f"org.apache.spark:spark-streaming-kafka-0-10_{scala_version}:{spark_version}",
        f"org.apache.spark:spark-sql-kafka-0-10_{scala_version}:{spark_version}",
        f"org.apache.kafka:kafka-clients:{kafka_version}",
    ]
    # Create a SparkSession
    # spark = (
    #     SparkSession.builder.master("local[*]")
    #     .appName("KafkaToSpark")
    #     .config("spark.jars.packages", ",".join(packages))
    #     .getOrCreate()
    # )
    spark = SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()

    # Read data from Kafka
    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", f"{host}:{port}")
        .option("subscribe", topic)
        .load()
    )

    # Extract message value
    df = df.selectExpr("CAST(value AS STRING) AS message")

    # Print the messages to the console
    df.writeStream.outputMode("append").format("console").option(
        "truncate", False
    ).start().awaitTermination()


if __name__ == "__main__":
    kafka_host = "kafka-svc"
    kafka_topic = "debezium.public.loggings"
    port = "9092"
    spark_streaming(kafka_host, kafka_topic, port)
