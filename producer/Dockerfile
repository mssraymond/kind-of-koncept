FROM python:3.9-slim
WORKDIR /app
COPY producer/producer.py .
RUN pip install --upgrade pip && \
    pip install confluent-kafka[json,schemaregistry]
CMD ["python", "producer.py"]