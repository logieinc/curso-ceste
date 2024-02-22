from venv import logger

import boto3

s3 = boto3.client('s3')

def procesar_s3_csv(bucket_name, archivo):
    resp = s3.select_object_content(
        Bucket=bucket_name,
        Key=archivo,
        ExpressionType='SQL',
        Expression="SELECT * FROM s3object s where s.\"Name\" = 'Jane'",
        InputSerialization = {'CSV': {"FileHeaderInfo": "Use"}, 'CompressionType': 'NONE'},
        OutputSerialization = {'CSV': {}},
    )
    print("")
    for event in resp['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')
            print(records)
        elif 'Stats' in event:
            statsDetails = event['Stats']['Details']
            print(f"Detalles de estadísticas bytes escaneados: {statsDetails['BytesScanned']}")
            print(f"Detalles de estadísticas bytes procesados: {statsDetails['BytesProcessed']} ")
            print(f"Bytes de detalles de estadísticas devueltos: {statsDetails['BytesReturned']}")

if __name__ == "__main__":
    try:
        procesar_s3_csv('my-bucket-ceste', 'sample_data.csv')
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")