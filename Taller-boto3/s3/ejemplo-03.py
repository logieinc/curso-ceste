from venv import logger

import boto3

# Cargar archivo a bucket
def cargar_archivo(bucket_name, archivo, name_in_bucket):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).upload_file(archivo, name_in_bucket)
    print("Archivo cargado")
    return 0


# Descargar archivo de bucket con otro nombre
def descargar_archivo_con_nombre(bucket_name, archivo, nombre):
    s3 = boto3.resource('s3')
    s3.Bucket(bucket_name).download_file(archivo, nombre)
    print("Archivo descargado")
    return 0

# Obtener permisos ACL archivo en bucket
def obtener_permisos_acl(bucket_name, archivo):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, archivo)
    print(obj.Acl())
    return 0

if __name__ == "__main__":
    try:
        cargar_archivo('my-bucket-ceste', 'resources/logo-ceste.png', 'logo-ceste.png')
        descargar_archivo_con_nombre('my-bucket-ceste', 'logo-ceste.png', 'resources/logo-ceste-2.png')
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")