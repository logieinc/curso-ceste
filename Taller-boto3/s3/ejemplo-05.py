from venv import logger

import boto3

BUCKET_NAME = "ceste-lab-bucket-fabian"
REGION_NAME = "us-east-1"
RESOURCE_TO_LOAD = 'resources/sample_data.csv.gz'
OBJECT_LOADED_NAME = 'sample_data.csv.gz'

s3 = boto3.client('s3')

def cargar_archivo(bucket_name, archivo, name_in_bucket):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).upload_file(archivo, name_in_bucket)
    print("Archivo cargado")
    return 0

def procesar_s3_csv_gz(bucket_name, archivo):
    resp = s3.select_object_content(
        Bucket=bucket_name,
        Key=archivo,
        ExpressionType='SQL',
        Expression="SELECT * FROM s3object s where s.\"Name\" = 'Jane'",
        InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'GZIP'},
        OutputSerialization = {'CSV': {}},
    )
    print("")
    for event in resp['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            print(records)
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print("Stats details bytesScanned: ")
            print(statsDetails['BytesScanned'])
            print("Stats details bytesProcessed: ")
            print(statsDetails['BytesProcessed'])
            print("Stats details bytesReturned: ")
            print(statsDetails['BytesReturned'])


if __name__ == "__main__":
    try:
        cargar_archivo(BUCKET_NAME, RESOURCE_TO_LOAD, OBJECT_LOADED_NAME)
        procesar_s3_csv_gz(BUCKET_NAME, OBJECT_LOADED_NAME)
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")