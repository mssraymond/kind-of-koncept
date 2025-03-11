FROM spark:3.5.3
USER root
WORKDIR /app
COPY spark/spark.py .
RUN pip install --upgrade pip && \
    pip install psycopg2-binary
CMD ["python", "spark.py"]