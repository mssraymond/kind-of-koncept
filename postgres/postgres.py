import psycopg2


def query_table(host, database, user, password, schema, table_name):
    """
    Queries the specified table in a PostgreSQL database. Returns list of tuples, where each tuple represents a row from the table.
    Returns None if an error occurs.
    """
    try:
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
        )
        cur = conn.cursor()

        cur.execute(f"SELECT * FROM {schema}.{table_name};")

        rows = cur.fetchall()

        cur.close()
        conn.close()

        return rows

    except psycopg2.Error as e:
        print(f"Error connecting to or querying the database: {e}")
        return None


if __name__ == "__main__":
    host = "postgres-svc"
    database = "postgres"
    user = "postgres"
    password = "postgres"
    schema = "public"
    table_name = "loggings"

    results = query_table(host, database, user, password, schema, table_name)

    if results is not None:
        for row in results:
            print(row)
