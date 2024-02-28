import json

import boto3
# Replace with your RDS credentials (IAM role with necessary permissions)
client = boto3.client('rds')

CLUSTER_IDENTIFIER = 'database-2'

def query_db_clusters():
    try:
        response = client.describe_db_clusters(DBClusterIdentifier=CLUSTER_IDENTIFIER)
        print()
        print("-" * 80)
        print(json.dumps(response['ResponseMetadata'], indent=2))
        print("-" * 80)

    except client.exceptions.DBClusterNotFoundFault as e:
        print(f"Cluster '{CLUSTER_IDENTIFIER}' no encontrado : {e}")

    except client.exceptions.ClientError as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
        query_db_clusters()