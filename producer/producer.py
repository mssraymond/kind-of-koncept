import datetime
import logging
import os
import random
import time

from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.json_schema import JSONSerializer
from confluent_kafka.serialization import MessageField, SerializationContext

logging.basicConfig(level=logging.INFO)

SCHEMA_STR = """{
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "LogMessage",
    "type": "object",
    "properties": {
        "timestamp": {
            "type": "string",
            "format": "date-time"
        },
        "worker_id": {
            "type": "string"
        }
    },
    "required": ["timestamp", "worker_id"]
}"""


# Wrapper function to pass to JSONSerializer
def log_message_to_dict(log_message, ctx):
    return log_message


def main():
    # Get environment variables
    producer_id = os.getenv("PRODUCER_ID")
    broker = os.getenv("KAFKA_BROKER")
    topic = os.getenv("KAFKA_TOPIC")
    schema_registry_url = os.getenv("SCHEMA_REGISTRY_URL")

    # Initialize Schema Registry Client
    schema_registry_conf = {"url": schema_registry_url}
    schema_registry_client = SchemaRegistryClient(schema_registry_conf)

    # Initialize JSON Serializer
    json_serializer = JSONSerializer(
        SCHEMA_STR, schema_registry_client, log_message_to_dict
    )

    # Initialize Kafka producer
    producer_conf = {"bootstrap.servers": broker}
    producer = Producer(producer_conf)

    logging.info(f"Worker {producer_id} started...")

    # Continuously emit messages
    while True:
        sleep_duration = random.randint(1, 9)
        time.sleep(sleep_duration)
        current_time = datetime.datetime.now().isoformat()
        message = {"timestamp": current_time, "worker_id": producer_id}
        producer.produce(
            topic=topic,
            key=producer_id,
            value=json_serializer(
                message, SerializationContext(topic, MessageField.VALUE)
            ),
            on_delivery=lambda err, msg: logging.info(
                f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}"
            ),
        )
        producer.flush()
        logging.info(f"Worker {producer_id} emitted message at {current_time}")


if __name__ == "__main__":
    main()
