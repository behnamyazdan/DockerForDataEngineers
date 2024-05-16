import json
import os
import psycopg2
import redis
from datetime import datetime
from psycopg2 import Error

# Reading database credentials from environment variables
db_user = os.environ.get("DB_USER", "postgres")
db_password = os.environ.get("DB_PASSWORD", "postgres")
db_host = os.environ.get("DB_HOST", "127.0.0.1")
db_port = os.environ.get("DB_PORT", "54321")
db_name = os.environ.get("DB_NAME", "ecommerce_docker")

try:
    connection = psycopg2.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port,
        database=db_name
    )

    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS clickstream (
                                id SERIAL PRIMARY KEY,
                                user_id INT NOT NULL,
                                page_title VARCHAR(255),
                                page_url VARCHAR(450),
                                timestamp TIMESTAMP(0),
                                event_type VARCHAR(20)
                            );'''

    cursor.execute(create_table_query)
    connection.commit()
    print("Table created successfully in PostgreSQL")

    # Assuming you already have a function to parse JSON data
    insert_query = '''INSERT INTO clickstream (user_id, page_title, page_url, timestamp, event_type)
                    VALUES (%s, %s, %s, %s, %s);'''

    r = redis.Redis(host='127.0.0.1', port=6379)
    while True:
        data = r.blpop('clickstream_queue')
        data_json = json.loads(data[1])
        record_to_insert = (data_json['user_id'], data_json['page_title'], data_json['page_url'],
                            data_json['timestamp'], data_json['event_type'])
        cursor.execute(insert_query, record_to_insert)
        connection.commit()
        print("{} - Inserted record into database".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))


except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
