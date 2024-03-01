from venv import logger

import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "ceste-lab-bucket-fabian"
REGION_NAME = "us-east-1"
RESOURCE_TO_LOAD = 'resources/sample_data.csv'
OBJECT_LOADED_NAME = 'sample_data.csv'

s3 = boto3.client('s3')

# Crear funcion para separar nombre archivo y extension, devoliendo solo nombre
def obtener_nombre_archivo(archivo):
    nombre_archivo, extension = archivo.split('.')
    return nombre_archivo

def obtener_extension_archivo(archivo):
    nombre_archivo, extension = archivo.split('.')
    return extension

def cargar_archivo(bucket_name, archivo, name_in_bucket):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).upload_file(archivo, name_in_bucket)
    print("Archivo cargado")
    return 0

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


def descargar_s3_csv_versioned(object_loaded_name, version_id):
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=object_loaded_name, VersionId=version_id)
        with open(f'downloaded/{obtener_nombre_archivo(object_loaded_name)}_{version_id}.{obtener_extension_archivo(object_loaded_name)}', 'wb') as f:
            f.write(response['Body'].read())
    except ClientError as e:
        print(f"Error al descargar la versión del objeto: {e} -> {version_id}")
        raise e


def obtener_lista_versiones_archivo_s3(bucket_name: str, object_key: str) -> list:
  """
  Obtiene una lista de las versiones de un archivo en un bucket de S3.

  Parámetros:
    bucket_name (str): Nombre del bucket que contiene el archivo.
    object_key (str): Nombre del archivo a obtener la lista de versiones.

  Retorno:
    list: Lista de diccionarios con información de cada versión del archivo.
  """
  try:
    s3 = boto3.client('s3')
    response = s3.list_object_versions(Bucket=bucket_name, Prefix=object_key)
    versiones = []
    for version in response['Versions']:
      versiones.append({
        'VersionId': version['VersionId'],
        'IsLatest': version['IsLatest'],
        'LastModified': version['LastModified'],
        'Size': version['Size']
      })
    return versiones
  except ClientError as e:
    raise ValueError(f"Error al obtener lista de versiones: {e}")



if __name__ == "__main__":
    try:
        cargar_archivo(BUCKET_NAME, RESOURCE_TO_LOAD, OBJECT_LOADED_NAME)
        procesar_s3_csv(BUCKET_NAME, OBJECT_LOADED_NAME)
        lista_versiones = obtener_lista_versiones_archivo_s3(BUCKET_NAME, OBJECT_LOADED_NAME)
        for version in lista_versiones:
            print(f"Versión: {version['VersionId']}")
            print(f"  Última versión: {version['IsLatest']}")
            print(f"  Fecha de modificación: {version['LastModified']}")
            print(f"  Tamaño: {version['Size']} bytes")
            if not version['IsLatest']:
                descargar_s3_csv_versioned(OBJECT_LOADED_NAME, version['VersionId'])
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")

