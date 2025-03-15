FROM spark:3.5.1
USER root
WORKDIR /app
COPY python/pg.py .
RUN pip install --upgrade pip && \
    pip install psycopg2-binary
CMD ["python", "pg.py"]