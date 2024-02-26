from venv import logger

import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "ceste-test-bucket-name-3"
REGION_NAME = "us-east-1"
VERSIONED = False

class BucketWrapper:
    """Encapsula S3 acciones buckets."""

    def __init__(self, bucket):
        """
        :param bucket: un recurso del depósito Boto3. Este es un recurso de alto nivel en Boto3.
                       que envuelve las acciones del bucket en una estructura similar a una clase.
        """
        self.bucket = bucket
        self.name = bucket.name


    def create(self, region_override=None, versioned=False):
        """
        Cree un bucket de Amazon S3 en la región predeterminada de la cuenta o en la Región especificada.

        :param region_override: la región en la que se creará el bucket. Si esto es
                                no especificado, la Región configurada en su compartido
                                Se utilizan credenciales.
        """
        if region_override is not None:
            region = region_override
        else:
            region = self.bucket.meta.client.meta.region_name
        try:
            #self.bucket.create(CreateBucketConfiguration={"LocationConstraint": "us-east-1"})
            self.bucket.create()
            self.bucket.wait_until_exists()
            # Habilitar el control de versiones para el bucket
            if versioned:
                self.bucket.Versioning().enable()
            logger.info("Bucket creado '%s' en region=%s", self.bucket.name, region)
        except ClientError as error:
            logger.exception(
                "No puedo crear bucket  '%s' en region=%s.",
                self.bucket.name,
                region,
            )
            raise error

if __name__ == "__main__":
    try:
        s3_resource = boto3.resource("s3")
        # Reemplazar ceste-test-bucket-name-1 por otro nombre
        wrapper = BucketWrapper(s3_resource.Bucket(BUCKET_NAME))
        wrapper.create(region_override=REGION_NAME, versioned=VERSIONED)
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")



