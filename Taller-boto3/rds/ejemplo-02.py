import json
from venv import logger
import pymysql

# Replace with your RDS credentials
DATABASE = 'databaseceste'
USERNAME = 'admin'
PASSWORD = 'admin1234'
HOST = 'database-1.c1ow0e2comct.us-east-1.rds.amazonaws.com'
PORT = 3306

def query_rds():
    # Create a connection to the RDS database
    try:
        connection = pymysql.connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            database=DATABASE,
            port=PORT
        )
        print()
        print("-" * 80)
        print("Conexion establecida exitosamente")
        print("-" * 80)
        # Execute your SQL queries here using connection.cursor()
        with connection.cursor() as cursor:
            # Example query
            cursor.execute("SELECT * FROM Transactions")
            # Imprimir registro a registro por consola
            for row in cursor.fetchall():
                print(row)
                print("-" * 80)

    except pymysql.Error as e:
        print(f"Error conectando a RDS: {e}")
    finally:
        # Remember to close the connection
        connection.close()
        print("Conexión cerrada")

if __name__ == "__main__":
    try:
        query_rds()
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")