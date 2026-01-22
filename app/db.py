
import mysql.connector
import os
from pandas import DataFrame


def get_dhe_env():
  host = os.getenv("HOST", "127.0.0.1")
  port = os.getenv("PORT", 3306)
  user = os.getenv("USER", "root")
  password = os.getenv("PASSWORD", "0533863104")
  database = os.getenv("DATABASE","test_database" )
  return host, port , user, password, database


def get_conn(host, port , user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password= password,
            database= database
        )
        if connection.is_connected():
            return connection
    except Exception as e:
       print(f"eror: {e}")

def init_databes():
    host, port , user, password, database = get_dhe_env()
    connection= get_conn(host, port , user, password, database)

    if connection is not None:
        cursor = connection.cursor(dictionary=True)

        cursor.execute('''

use `test_database`;
CREATE table IF not exists my_table (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    weapon_id varchar(255),
    weapon_name varchar(255),
    weapon_type varchar(255),
    range_km int,
    weight_kg float,
    manufacturer varchar(255),
    origin_country varchar(225),
    storage_location varchar(255),
    year_estimated int,
    risk_level varchar(255)
);

            ''')



    