from kafka import KafkaConsumer
import os
import logging

logging.basicConfig(level=logging.INFO)

def main():
    # Get environment variables for worker id and Kafka configuration
    broker = os.getenv("KAFKA_BROKER")
    topic = os.getenv("KAFKA_TOPIC")

    # Initialize Kafka producer with JSON serialization
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=broker
    )

    # Continuous loop: wait a random duration, then send a log message to Kafka
    for message in consumer:
        logging.info(message)

if __name__ == "__main__":
    main()
