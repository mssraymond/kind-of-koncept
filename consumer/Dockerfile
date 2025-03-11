FROM python:3.9-slim
WORKDIR /app
COPY consumer/consumer.py .
RUN pip install --upgrade pip && \
    pip install kafka-python
CMD ["python", "consumer.py"]