from venv import logger

"""

    Conectarse a base de datos utilizando usuario y password desde secretsmanager 

    Crear table en base de datos RDS
        CREATE TABLE twitter_data (
            country varchar(255) NOT NULL,
            retweets integer not null,
            favorites integer not null
        )

    Con pandas obtener groupby country sumatorio de retweets y favorites del archivo resources/twitter-data.csv
    
    Insertar resultado de tabla twitter_data de los datos obtenidos en pandas en RDS
    
    Mostrar por consola datos insertados
    
    Subir a S3 bucket el archivo resources/twitter-data.csv (opción puede ser zipeado)
    
    Realizar un select de un country determinado creando un archivo de salida en output/resultado.csv de dicha consulta
    

"""

if __name__ == "__main__":
    try:
        pass
    except Exception as e:
        logger.error(f"Un error desconocido ocurrió: {str(e)}.")