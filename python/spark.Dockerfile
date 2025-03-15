FROM spark:3.5.5
USER root
WORKDIR /app
COPY python/spark.py .
RUN pip install --upgrade pip
CMD ["python", "spark.py"]