import psycopg2
from config import config

def connect():
    connection = None
    try:
        params = config()
        print('connecting to the postgreSql database...')
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        create_table = '''CREATE TABLE edata(name varchar, address varchar, gender varchar);'''
        print('Table is creating!!')
        
        cursor.execute(create_table)
        connection.commit()
        print('Table is created successfully')

        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database connection Terminated!')

if __name__ == "__main__":
    connect()