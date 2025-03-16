from pyspark.sql import SparkSession


def spark_streaming(host, topic, port):
    spark = SparkSession.getActiveSession() or SparkSession.builder.getOrCreate()

    df = (
        spark.readStream.format("kafka")
        .option("kafka.bootstrap.servers", f"{host}:{port}")
        .option("subscribe", topic)
        .load()
    )

    df = df.selectExpr("CAST(value AS STRING) AS message")

    df.writeStream.outputMode("append").format("console").option(
        "truncate", False
    ).start().awaitTermination()


if __name__ == "__main__":
    kafka_host = "kafka-svc"
    kafka_topic = "debezium.public.loggings"
    port = "9092"
    spark_streaming(kafka_host, kafka_topic, port)
