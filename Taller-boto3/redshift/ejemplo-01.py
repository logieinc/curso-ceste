import os

import boto3
import psycopg2

try:
    redshift = boto3.client('redshift')
    cluster_identifier = 'redshift-cluster-1'  # Replace with your cluster's name
    db_user = 'awsuser'  # Replace with your Redshift database username
    db_password = 'Awsuser1234'  # Replace with your Redshift database password
    host = redshift.describe_clusters(ClusterIdentifier=cluster_identifier)['Clusters'][0]['Endpoint']['Address']
    port = redshift.describe_clusters(ClusterIdentifier=cluster_identifier)['Clusters'][0]['Endpoint']['Port']

    conn_string = f"postgresql://{db_user}:{db_password}@{host}:{port}/{cluster_identifier}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    # Execute your SQL queries here using the cursor object
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    print(rows)

    # Commit changes (if applicable)
    conn.commit()

except Exception as e:
    print(f"Error connecting to Redshift: {e}")
finally:
    # Close the connection and cursor
    if cursor:
        cursor.close()
    if conn:
        conn.close()
