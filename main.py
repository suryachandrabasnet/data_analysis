import psycopg2
import csv
from config import config
from sql_queries import edata_to_create, edata_to_insert

def connect():
    connection = None
    try:
        params = config()
        print('connecting to the postgreSql database...')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()

        # create table
        # create_table = edata_to_create
        # print('Table is created!!')
        
        # cursor.execute(create_table)
        # connection.commit()
        # print('Table is created successfully')

        # insert data
        with open('data/data.csv',encoding= 'unicode_escape') as f:
            reader = csv.reader(f)
            for row in reader:
                cursor.execute(edata_to_insert, row)

        connection.commit()
        cursor.close()

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection Terminated!')

if __name__ == "__main__":
    connect()