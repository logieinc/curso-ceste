"""
    Conexion AWS RDS

    CREATE DATABASE Transactions_Prod;

    USE Transactions_Prod;

    CREATE TABLE Transactions (
        transaction_id INT PRIMARY KEY,
        amount DECIMAL(13,2) NOT NULL,
        transaction_type ENUM('PURCHARSE', 'REFUND') NOT NULL
    )

    desc Transactions;

"""
import json
from venv import logger
import boto3

rds_client = boto3.client('rds')

def conectar_rds():

    response = rds_client.describe_db_instances()
    print()
    print("-" * 80)
    for db in response['DBInstances']:
        print(json.dumps(db, indent=2, default=str))
        print("-" * 80)


if __name__ == "__main__":
    try:
        conectar_rds()
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")

