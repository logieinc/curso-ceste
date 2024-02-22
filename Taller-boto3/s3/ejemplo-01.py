from venv import logger

import boto3

def hola_s3():
    """
        Utilice AWS SDK para Python (Boto3) para crear un servicio de almacenamiento simple de Amazon
        (Amazon S3) y enumere los depósitos en su cuenta.
        Este ejemplo utiliza la configuración predeterminada especificada en sus credenciales compartidas.
        y archivos de configuración.
    """
    s3_resource = boto3.resource("s3")
    print("")
    print("Amazon S3! Let's lista de sus buckets:")
    for bucket in s3_resource.buckets.all():
        print(f"\t{bucket.name}")

if __name__ == "__main__":
    try:
        hola_s3()
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")
