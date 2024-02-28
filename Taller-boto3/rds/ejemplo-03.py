import json
from venv import logger

import boto3

DATABASE_NAME = 'databasecestepostgres'
DB_CLUSTER_ARN = 'arn:aws:rds:us-east-1:027043390897:cluster:database-2'
DB_CREDENTIALS_SECRET_STORE_ARN = 'arn:aws:secretsmanager:us-east-1:027043390897:secret:rds-db-credentials/cluster-2MMUVZ2SO6AYHPG65GVDT4N5YE/postgres/1709152575500-PNQibc'
SQL = 'SELECT * FROM Transactions'
# sql = 'select * from information_schema.tables'

def query_rds_aurora():
    # Replace with your RDS credentials (IAM role with necessary permissions)
    client = boto3.client('rds-data')

    parameters = []
    response = client.execute_statement(
        secretArn=DB_CREDENTIALS_SECRET_STORE_ARN,
        database=DATABASE_NAME,
        resourceArn=DB_CLUSTER_ARN,
        sql=SQL,
        parameters=parameters
    )
    print("-" * 80)
    print(json.dumps(response, indent=2))
    print("-" * 80)
    for row in response['records']:
        print(row)
        print("-" * 80)

if __name__ == "__main__":
    try:
        query_rds_aurora()
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")
