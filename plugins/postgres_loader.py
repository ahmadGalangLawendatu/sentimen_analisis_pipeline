from sqlalchemy import create_engine


def get_connection():
    user = 'airflow'
    passwd = 'airflow'
    hostname = 'localhost'
    port = 5437
    database = 'data_warehouse'

    conn_string = f'postgresql://{user}:{passwd}@{hostname}:5437/{database}'
    return create_engine(conn_string)


def load(data, table_name):
    conn = get_connection()

    try:
        data.to_sql(table_name, conn, if_exists='append', index=False)
        print("Successfully loaded to PostgreSQL")
    except Exception as e:
        print(f"Error loading data to PostgreSQL: {str(e)}")
    finally:
        conn.dispose()
