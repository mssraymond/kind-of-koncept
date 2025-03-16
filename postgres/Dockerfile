FROM spark:3.5.5
USER root
WORKDIR /app
COPY postgres/postgres.py .
RUN pip install --upgrade pip && \
    pip install psycopg2-binary
CMD ["python", "postgres.py"]