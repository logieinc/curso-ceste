"""
    Obtener secrets desde AWS
"""
import json
import logging
from venv import logger

import boto3

SECRET_NAME = "secreto/database"
REGION_NAME = "us-east-1"

class GetSecretWrapper:
    def __init__(self, secretsmanager_client):
        self.client = secretsmanager_client

    def get_secret(self, secret_name):
        """
        Recupera secretos individuales de AWS Secrets Manager mediante la API get_secret_value.
        Esta función supone que la pila mencionada en el código fuente README se ha implementado correctamente.
        Esta pila incluye 7 secretos, todos los cuales tienen nombres que comienzan con "mySecret".

        :param secret_name: el nombre del secreto obtenido.
        : escriba nombre_secreto: cadena
        """
        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
            logging.info("Secreto recuperado con éxito.")
            return get_secret_value_response["SecretString"]
        except self.client.exceptions.ResourceNotFoundException:
            msg = f"El secreto solicitado {secret_name} no fue encontrado."
            logger.info(msg)
            return msg
        except Exception as e:
            raise e

    def get_clave_valor(self, secret_name):
        """
        Recupera secretos individuales de AWS Secrets Manager mediante la API get_secret_value.
        Esta función supone que la pila mencionada en el código fuente README se ha implementado correctamente.
        Esta pila incluye 7 secretos, todos los cuales tienen nombres que comienzan con "mySecret".

        :param secret_name: el nombre del secreto obtenido.
        : escriba nombre_secreto: cadena
        """
        try:
            get_secret_value_response = self.client.get_secret_value(
                SecretId=secret_name
            )
            logging.info("Secreto recuperado con éxito.")
            data = json.loads(get_secret_value_response["SecretString"])
            for clave, valor in data.items():
                print(f"Clave: {clave}, Valor: {valor}")
            return clave, valor
        except self.client.exceptions.ResourceNotFoundException:
            msg = f"El secreto solicitado {secret_name} no fue encontrado."
            logger.info(msg)
            return msg
        except Exception as e:
            raise e


if __name__ == "__main__":
    try:
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=REGION_NAME
        )
        print("")
        print("-" * 80)
        print(GetSecretWrapper(client).get_secret(SECRET_NAME))
        print("-" * 80)
        print(GetSecretWrapper(client).get_clave_valor(SECRET_NAME))
        print("-" * 80)
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")
