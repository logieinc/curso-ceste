BOTO3
-----

<br >![ Screenshot of the empty token dialog box ](assets/images/boto3.jpg)

### Boto3: El SDK de Python para AWS

**¿Qué es boto3?**

- **SDK de AWS para Python:** Boto3 es el SDK oficial de Python para interactuar con los recursos de Amazon Web Services (AWS). Proporciona APIs completas para más de 160 servicios de AWS, incluyendo:
    - Almacenamiento (S3, Glacier, EBS)
    - Computación (EC2, Lambda, ECS)
    - Bases de datos (DynamoDB, RDS)
    - Redes (VPC, Route 53)
    - Aprendizaje automático (SageMaker, Rekognition)
    - Administración y gestión (IAM, CloudWatch)
    - ...¡y muchos más!

**Características principales:**

- **Abstracciones de alto nivel:** Simplifica las interacciones con servicios AWS complejos, promoviendo un código limpio y legible.
- **Gestión automática de detalles de bajo nivel:** Se encarga de las credenciales de AWS, la firma de solicitudes y la gestión de errores, ahorrándote tiempo y esfuerzo.
- **APIs potentes:** Ofrece control granular sobre diversas características de los servicios AWS, permitiendo diversos casos de uso.
- **Waiters y paginadores:** Mecanismos integrados para esperar eficientemente a que los recursos estén en el estado deseado y recuperar resultados paginados, respectivamente.
- **Context managers:** Agiliza la gestión de errores y la limpieza de recursos con el cierre automático de conexiones y la liberación de recursos.

**Casos de uso comunes:**

- **Administración del almacenamiento S3:** Carga, descarga, listado y manipulación de objetos en buckets de Amazon S3.
- **Creación y gestión de instancias EC2:** Lanzamiento, parada, terminación y configuración de instancias EC2.
- **Trabajo con tablas DynamoDB:** Creación, consulta, actualización y eliminación de elementos en tablas DynamoDB.
- **Automatización de implementaciones en AWS:** Gestión programática de la infraestructura y las configuraciones de los recursos.
- **Integración de los servicios AWS en las aplicaciones:** Aprovechamiento de las capacidades de AWS en sus proyectos basados en Python.

**Empezando:**

1. **Instalación:**
   ```bash
   pip install boto3
   ```

2. **Importar la biblioteca:**
   ```python
   import boto3
   ```

3. **Configurar las credenciales de AWS:**
   El enfoque más común es establecer variables de entorno:
   ```bash
   export AWS_ACCESS_KEY_ID="your_access_key_id"
   export AWS_SECRET_ACCESS_KEY="your_secret_access_key"
   ```
   Alternativamente, use un archivo de credenciales o roles IAM de instancia.

4. **Crear clientes u objetos de recursos:**
   ```python
   s3_client = boto3.client('s3')  # Cliente para interactuar con el servicio S3
   ec2_resource = boto3.resource('ec2')  # Recurso para crear y administrar instancias EC2
   ```

5. **Comenzar a utilizar los métodos de la API:**
   ```python
   # Subir un archivo a S3
   s3_client.upload_file(Filename="path/to/your/file.txt", 
                            Bucket="your-bucket-name", 
                            Key="my_file.txt")

   # Crear una instancia EC2
   instance = ec2_resource.create_instances(
       ImageId="ami-0123456789abcdef0",
       MinCount=1,
       MaxCount=1,
       InstanceType="t2.micro"
   )

   # Imprimir detalles de la instancia
   print(instance.id, instance.state)
   ```



