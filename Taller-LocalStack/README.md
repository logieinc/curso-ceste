
# LocalStack

LocalStack es una excelente herramienta para simular servicios de AWS de manera local, ideal para el desarrollo y pruebas sin incurrir en costos adicionales de AWS. Aquí tienes una guía básica para preparar un taller sobre LocalStack:


## Características LocalStack


**Características de LocalStack:**

1.	**Simulación de servicios de AWS:**
•	LocalStack permite emular más de 60 servicios de AWS, como S3, Lambda, DynamoDB, API Gateway, SQS, SNS, y más.
2.	**Compatibilidad con múltiples entornos:**
•	Funciona en cualquier entorno que soporte Docker, lo que lo hace fácil de usar en máquinas locales, servidores o pipelines CI/CD.
3.	**Despliegue rápido y local:**
•	Puedes levantar y configurar un entorno completo de AWS en tu máquina local en pocos segundos, eliminando la necesidad de configurar infraestructuras complejas en la nube.
4.	**Soporte para múltiples lenguajes:**
•	Permite ejecutar funciones Lambda en varios runtimes como Node.js, Python, Java, Go, entre otros.
5.	**Simulación de API Gateway:**
•	Emula API Gateway para desarrollar y probar API REST que interactúan con Lambdas y otros servicios.
6.	**Pruebas de integración automatizadas:**
•	Integración perfecta con entornos de pruebas, lo que permite realizar tests automatizados sin depender de servicios externos o la conexión a internet.
7.	**Fácil integración con herramientas de desarrollo:**
•	Compatible con herramientas populares como AWS CLI, SDKs de AWS y Terraform, lo que facilita la creación de infraestructuras locales similares a las que se usarían en AWS real.
8.	**Modos de operación estándar y pro:**
•	La versión estándar es gratuita y soporta una amplia gama de servicios. La versión Pro añade características avanzadas como la simulación de servicios más complejos (RDS, Elasticsearch, etc.), UI mejorada y más herramientas de depuración.
9.	**Persistencia de datos:**
•	Permite la opción de persistir los datos en el disco para pruebas repetibles, simulando más de cerca un entorno de producción.

**Beneficios de usar LocalStack:**

1.	**Ahorro de costos:**
•	No necesitas realizar pruebas directamente en AWS, lo que te ahorra costos en servicios como S3, DynamoDB, y Lambda mientras desarrollas y pruebas.
2.	**Desarrollo sin conexión a internet:**
•	Al trabajar localmente, no dependes de una conexión a internet o del acceso a AWS, permitiendo mayor independencia y velocidad en el desarrollo.
3.	**Pruebas rápidas y seguras:**
•	Permite probar cambios y ejecutar pruebas sin afectar recursos en la nube real ni correr riesgos de errores en producción.
4.	**Mayor productividad en el desarrollo:**
•	Al simular AWS en tu entorno local, puedes desarrollar y probar de manera más ágil sin tener que esperar despliegues largos ni lidiar con tiempos de respuesta de la nube.
5.	**Pruebas locales de pipelines CI/CD:**
•	Ideal para integrarse con pipelines de integración continua (CI) y despliegue continuo (CD), permitiendo ejecutar pruebas de integración sin depender de AWS real.
6.	**Entorno de pruebas aislado:**
•	Crea un entorno controlado y reproducible para probar flujos complejos de AWS sin interactuar con entornos de producción.
7.	**Iteración rápida:**
•	Al simular AWS localmente, puedes realizar iteraciones rápidas en el desarrollo, depuración y pruebas, mejorando el flujo de trabajo general.
8.	**Desarrollo multi-servicio:**
•	Permite interactuar con varios servicios de AWS en conjunto (por ejemplo, Lambda, S3, y DynamoDB), probando flujos reales de aplicaciones distribuidas.


## Instalación de LocalStack

- **Requisitos previos:**
- Docker (LocalStack funciona sobre Docker).
- Python (para instalar la CLI de LocalStack, opcionalmente).

- **Pasos de instalación:**
- Instalar Docker.
- Instalar LocalStack:

```shell
   pip install localstack
```

- Levantar LocalStack:

```shell
   localstack start
```
- **Usar con Docker Compose (alternativa popular):**
- Crear un archivo docker-compose.yml:

```yaml
version: '3.8'
      services:
      localstack:
         image: localstack/localstack
         container_name: localstack
         ports:
            - "4566:4566"
            - "4571:4571"
         environment:
            - SERVICES=s3,dynamodb,lambda,sqs
            - DEBUG=1
         volumes:
            - "./localstack:/var/lib/localstack"
```

- Levantar los servicios:

```shell
   docker-compose up
```

- **Configuración de AWS CLI para LocalStack**

- Instalar AWS CLI:

```shell
   pip install awscli
```

- Configurar AWS CLI para conectarse a LocalStack:

```shell
   aws configure
   # Usar valores dummy como:
   # AWS Access Key ID: test
   # AWS Secret Access Key: test
   # Default region name: us-east-1
   # Default output format: json
```

- **Configurar el endpoint local para que AWS CLI use LocalStack:**
- Ejemplo para S3:

```shell
      aws --endpoint-url=http://localhost:4566 s3 ls
```

**Ejemplos prácticos**

**Crear un bucket en S3:**

```shell
      aws --endpoint-url=http://localhost:4566 s3 mb s3://mi-bucket
```

**Subir un archivo a S3:**

```shell
      echo "Hola LocalStack" > archivo.txt
      aws --endpoint-url=http://localhost:4566 s3 cp archivo.txt s3://mi-bucket/
```

**Listar objetos en el bucket:**

```shell
      aws --endpoint-url=http://localhost:4566 s3 ls s3://mi-bucket/
```

**Crear una tabla en DynamoDB:**

```shell
      aws --endpoint-url=http://localhost:4566 dynamodb create-table \
      --table-name MiTabla \
      --attribute-definitions AttributeName=Id,AttributeType=S \
      --key-schema AttributeName=Id,KeyType=HASH \
      --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
```

**Enviar un mensaje a SQS**

```shell
      aws --endpoint-url=http://localhost:4566 sqs create-queue --queue-name MiCola
      aws --endpoint-url=http://localhost:4566 sqs send-message --queue-url http://localhost:4566/000000000000/MiCola --message-body "Mensaje de prueba"
```

## Integración de LocalStack con otros servicios

	•	Integración con Lambda:
	•	Puedes subir y probar funciones Lambda localmente.
	•	Usa contenedores de Lambda y emulación de servicios como API Gateway.
	•	Integración con CI/CD:
	•	Cómo usar LocalStack en pipelines de Jenkins o GitLab para pruebas automatizadas.

## Práctica guiada

	•	Desarrollar una aplicación simple que use varios servicios de AWS, como S3, DynamoDB, Lambda y SQS, y hacer que los participantes simulen todo el flujo usando LocalStack.
	•	Puedes proporcionar ejercicios específicos como:
	•	Crear una API que guarde datos en DynamoDB usando Lambda.
	•	Enviar mensajes entre servicios usando SQS.

## Ejecución lambdas en LocalStack

Crear y ejecutar funciones Lambda en LocalStack es bastante sencillo, ya que simula el entorno de AWS Lambda de forma local. A continuación, te guiaré paso a paso para que puedas configurar y ejecutar Lambdas usando LocalStack.

**Configuración Inicial**

Asegúrate de tener LocalStack y AWS CLI configurados correctamente.

- Instala LocalStack y asegúrate de que el servicio Lambda esté habilitado en tu docker-compose.yml:

```shell
version: '3.8'
      services:
      localstack:
         image: localstack/localstack
         container_name: localstack
         ports:
            - "4566:4566"
            - "4571:4571"
         environment:
            - SERVICES=lambda,s3,dynamodb,sqs
            - DEBUG=1
         volumes:
            - "./localstack:/var/lib/localstack"
```

- Levanta LocalStack con Docker Compose:

```shell
      docker-compose up
```

**Escribir la Función Lambda**

Las funciones Lambda pueden ser escritas en varios lenguajes, como Node.js, Python, entre otros. Aquí vamos a usar un ejemplo básico en Node.js.

- Crea un archivo Lambda en Node.js, llamado lambda_function.js:

```json
      exports.handler = async (event) => {
         console.log('Evento recibido:', JSON.stringify(event, null, 2));
         return {
            statusCode: 200,
            body: JSON.stringify({
                  message: 'Hola desde Lambda LocalStack!',
                  input: event
            }),
         };
      };
```

Esta función simplemente imprime el evento recibido y devuelve un mensaje.

**Empaquetar la Lambda**

Para crear una función Lambda en AWS (o LocalStack), necesitas empaquetar tu código en un archivo .zip.

- Empaqueta el código en un archivo .zip:

```shell
      zip lambda_function.zip lambda_function.js
```

**Crear la Lambda en LocalStack**

Ahora que tienes tu función empaquetada, puedes crearla en LocalStack usando el AWS CLI.

- Crea la función Lambda en LocalStack:

```shell
      aws --endpoint-url=http://localhost:4566 lambda create-function \
      --function-name MiLambda \
      --runtime nodejs14.x \
      --role arn:aws:iam::000000000000:role/lambda-role \
      --handler lambda_function.handler \
      --zip-file fileb://lambda_function.zip
```

Aquí estamos creando una función llamada MiLambda con Node.js 14.x como runtime. El handler especifica qué función dentro del archivo ejecutará Lambda (en este caso, lambda_function.handler).

**Ejecutar la Lambda**

Una vez que la función Lambda ha sido creada, puedes invocarla usando la CLI.

- Invoca la Lambda con un evento de prueba:

```shell
      aws --endpoint-url=http://localhost:4566 lambda invoke \
      --function-name MiLambda \
      --payload '{"mensaje": "Este es un test"}' \
      response.json
```

Esto ejecutará la función Lambda y guardará la respuesta en un archivo llamado response.json.

**Verifica la respuesta:**

```shell
      cat response.json    
```

Deberías ver algo como:

```json
      {
         "statusCode": 200,
         "body": "{\"message\":\"Hola desde Lambda LocalStack!\",\"input\":{\"mensaje\":\"Este es un test\"}}"
      }
```

## Ejemplos avanzados

Puedes ir un paso más allá y conectar esta Lambda con otros servicios como S3, DynamoDB, o SQS. Aquí tienes un ejemplo de cómo hacerlo:

- Invocar una Lambda automáticamente desde S3:
- Crear un bucket S3 en LocalStack:

```json
      aws --endpoint-url=http://localhost:4566 s3 mb s3://mi-bucket
```

- Configurar un trigger en Lambda para que se ejecute cuando un archivo se suba a S3:

```json
      aws --endpoint-url=http://localhost:4566 lambda add-permission \
      --function-name MiLambda \
      --statement-id MiPermisoS3 \
      --action "lambda:InvokeFunction" \
      --principal s3.amazonaws.com \
      --source-arn arn:aws:s3:::mi-bucket

      aws --endpoint-url=http://localhost:4566 s3api put-bucket-notification-configuration \
      --bucket mi-bucket \
      --notification-configuration '{
            "LambdaFunctionConfigurations": [
               {
                  "LambdaFunctionArn": "arn:aws:lambda:us-east-1:000000000000:function:MiLambda",
                  "Events": ["s3:ObjectCreated:*"]
               }
            ]
      }'
```

Ahora, cada vez que subas un archivo a mi-bucket, se invocará la Lambda.

**Subir un archivo a S3 y verificar la invocación de Lambda:**

```shell
      echo "Este es un archivo de prueba" > archivo.txt
      aws --endpoint-url=http://localhost:4566 s3 cp archivo.txt s3://mi-bucket/
```

La Lambda se ejecutará automáticamente y podrás ver el evento de S3 en los logs de LocalStack.


**Monitoreo y Logs**

Puedes verificar los logs de tu función Lambda utilizando el servicio de logs simulado de LocalStack.

- Ver los logs de la Lambda:

```shell
      aws --endpoint-url=http://localhost:4566 logs describe-log-streams --log-group-name /aws/lambda/MiLambda
      aws --endpoint-url=http://localhost:4566 logs get-log-events --log-group-name /aws/lambda/MiLambda --log-stream-name <log-stream-name>
```

**Pruebas adicionales**

- Pruebas automatizadas: Implementa pruebas unitarias o de integración usando herramientas como Jest o Mocha, y configura LocalStack como parte de tu pipeline de CI.
- Interacciones complejas: Conectar Lambdas con DynamoDB, API Gateway, o crear workflows más avanzados simulando entornos reales de AWS.


## Pasos para crear un API Gateway en LocalStack que invoque una Lambda

**Configuración Inicial**

Asegúrate de que LocalStack esté corriendo con los servicios de Lambda y API Gateway habilitados en tu docker-compose.yml.

```yaml
      version: '3.8'
      services:
      localstack:
      image: localstack/localstack
      container_name: localstack
      ports:
            - "4566:4566"
            - "4571:4571"
      environment:
            - SERVICES=lambda,apigateway
            - DEBUG=1
      volumes:
            - "./localstack:/var/lib/localstack"
```

Levanta LocalStack con Docker Compose:

```shell
      docker-compose up
```

**Crear la Función Lambda**

Crea una función Lambda simple. Primero, escribe el código de la Lambda en un archivo llamado lambda_function.js:

```json
      exports.handler = async (event) => {
      const name = event.queryStringParameters?.name || 'mundo';
      return {
            statusCode: 200,
            body: JSON.stringify({
                  message: `¡Hola, ${name}!`
            }),
      };
      };
```

Esta función Lambda tomará un parámetro name de la consulta de la API y responderá con un saludo.

**Empaqueta la Lambda:**

```json
      zip lambda_function.zip lambda_function.js
```

**Crea la Lambda en LocalStack:**

```shell
      aws --endpoint-url=http://localhost:4566 lambda create-function \
      --function-name HolaLambda \
      --runtime nodejs14.x \
      --role arn:aws:iam::000000000000:role/lambda-role \
      --handler lambda_function.handler \
      --zip-file fileb://lambda_function.zip
```

**Crear API Gateway**

```shell
      aws --endpoint-url=http://localhost:4566 apigateway create-rest-api --name "MiAPI"
```

Esto devolverá el restApiId. Guárdalo para usarlo más adelante.

**Obtener el resourceId del recurso raíz:**

```shell
      aws --endpoint-url=http://localhost:4566 apigateway get-resources \
      --rest-api-id <restApiId>
```

El resourceId del recurso raíz (/) será el primer valor devuelto. Guárdalo también.

**Crear un nuevo recurso:**

Vamos a crear un recurso saludo que se vinculará a nuestra Lambda:

```shell
      aws --endpoint-url=http://localhost:4566 apigateway create-resource \
      --rest-api-id <restApiId> \
      --parent-id <resourceId> \
      --path-part saludo
```

Esto devolverá otro resourceId para el recurso /saludo.

**Crear el método GET en el recurso /saludo:**

```shell
      aws --endpoint-url=http://localhost:4566 apigateway put-method \
      --rest-api-id <restApiId> \
      --resource-id <resourceIdDelSaludo> \
      --http-method GET \
      --authorization-type "NONE"
```

**Vincular Lambda al método:**

Ahora conectemos la Lambda para que se ejecute cuando alguien haga una solicitud GET a /saludo.

**Establecer la integración entre API Gateway y Lambda:**

```shell
      aws --endpoint-url=http://localhost:4566 apigateway put-integration \
      --rest-api-id <restApiId> \
      --resource-id <resourceIdDelSaludo> \
      --http-method GET \
      --type AWS_PROXY \
      --integration-http-method POST \
      --uri arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:000000000000:function:HolaLambda/invocations
```

**Dar permiso a API Gateway para invocar la Lambda:**

```shell
      aws --endpoint-url=http://localhost:4566 lambda add-permission \
      --function-name HolaLambda \
      --statement-id api-gateway-access \
      --action lambda:InvokeFunction \
      --principal apigateway.amazonaws.com \
      --source-arn arn:aws:execute-api:us-east-1:000000000000:<restApiId>/*
```

**Desplegar la API**

Una vez configurada la API y su integración con Lambda, necesitamos desplegarla.

**Crear una nueva etapa de despliegue:**

```shell
      aws --endpoint-url=http://localhost:4566 apigateway create-deployment \
      --rest-api-id <restApiId> \
      --stage-name prod
```

**Probar la API**

Ahora puedes probar la API invocando el endpoint generado por API Gateway.

**Obtén el endpoint de la API:**

```shell
      http://localhost:4566/restapis/<restApiId>/prod/_user_request_/saludo?name=Juan
```

**Invoca la API usando curl:**

```shell
      curl "http://localhost:4566/restapis/<restApiId>/prod/_user_request_/saludo?name=Juan"
```

Deberías obtener una respuesta similar a:


```json
{
    "message": "¡Hola, Juan!"
}
```







