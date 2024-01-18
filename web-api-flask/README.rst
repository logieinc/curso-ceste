Conexión a API y Uso de Web APIs con Requests
--------------------------------------------------

**¿Qué es una Web API?**

Una Web API, o Application Programming Interface, es un conjunto de métodos y datos que se exponen a través de Internet para que los desarrolladores puedan interactuar con ellos. Las Web APIs se utilizan para una amplia gama de propósitos, como proporcionar acceso a datos, realizar tareas automatizadas o crear nuevas aplicaciones.

**¿Cómo funcionan las Web APIs?**

Las Web APIs se basan en el protocolo HTTP, que es el protocolo de comunicación estándar para la World Wide Web. Las solicitudes a una Web API se realizan utilizando el método HTTP GET o POST. El método GET se utiliza para recuperar datos de la API, mientras que el método POST se utiliza para enviar datos a la API.

**¿Cuáles son los tipos de Web APIs?**

Hay muchos tipos diferentes de Web APIs, pero algunas de las más comunes incluyen:

* **APIs RESTful:** Las APIs RESTful son las más comunes y se basan en el modelo REST. El modelo REST define una serie de convenciones para el diseño de APIs, como el uso de URIs para identificar recursos, el uso de verbos HTTP para indicar acciones y el uso de formatos de datos estándar, como JSON o XML.
* **APIs SOAP:** Las APIs SOAP son un tipo de API más antiguo que utiliza el protocolo SOAP. SOAP es un protocolo más complejo que REST, pero ofrece algunas ventajas, como el soporte para seguridad y transacciones.
* **APIs GraphQL:** Las APIs GraphQL son un tipo de API más reciente que ofrece una forma más flexible de interactuar con los datos. GraphQL permite a los desarrolladores solicitar solo los datos que necesitan, lo que puede mejorar el rendimiento y la eficiencia.

**¿Cuál es la importancia de las Web APIs?**

Las Web APIs son una herramienta esencial para el desarrollo web moderno. Las APIs se utilizan para una amplia gama de propósitos, como:

* **Acceso a datos:** Las APIs se pueden utilizar para acceder a datos de una variedad de fuentes, como bases de datos, sistemas de archivos o servicios en la nube.
* **Automatización de tareas:** Las APIs se pueden utilizar para automatizar tareas, como enviar correos electrónicos, procesar pagos o actualizar datos.
* **Creación de nuevas aplicaciones:** Las APIs se pueden utilizar para crear nuevas aplicaciones, como aplicaciones móviles, aplicaciones de escritorio o aplicaciones web.

Además de GET y POST, los métodos HTTP más utilizados en las Web APIs son:

* **PUT:** Se utiliza para actualizar datos en una API.
* **DELETE:** Se utiliza para eliminar datos de una API.
* **PATCH:** Se utiliza para actualizar parte de los datos en una API.
* **HEAD:** Se utiliza para obtener el encabezado de una respuesta HTTP.
* **OPTIONS:** Se utiliza para obtener información sobre los métodos HTTP admitidos por una API.

Estos métodos se utilizan para realizar diferentes acciones en una API, como:

* **GET:** Recuperar datos de una API.
* **POST:** Enviar datos a una API.
* **PUT:** Actualizar datos en una API.
* **DELETE:** Eliminar datos de una API.
* **PATCH:** Actualizar parte de los datos en una API.
* **HEAD:** Obtener el encabezado de una respuesta HTTP.
* **OPTIONS:** Obtener información sobre los métodos HTTP admitidos por una API.

En Python, estos métodos se pueden utilizar de la siguiente manera:

Todo es un objeto en Python:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ejemplo 01:

.. code:: python

    # Importar la biblioteca requests
    import requests
    import json

    # Realizar una solicitud GET
    headers = {"accept": "*/*"}
    response = requests.get('http://localhost:8000/api/people', headers=headers)

    # Obtener el contenido de la respuesta
    data = response.json()

    # Imprimir el contenido de la respuesta
    print(json.dumps(data, indent=2))

Ejemplo 02:

.. code:: python

    # Importar la biblioteca requests
    import requests
    import json

    # Realizar una solicitud POST
    headers = {"accept": "*/*", "Content-Type" : "application/json"}
    data = {'fname': 'John', 'lname': "Doe"}
    response = requests.post('http://localhost:8000/api/people', json=data, headers=headers)

    # Obtener el código de estado de la respuesta
    status_code = response.status_code
    data_response = response.json()

    # Imprimir el código de estado de la respuesta
    print()
    print(f"Status code => { status_code}")
    print()
    print(json.dumps(data_response, indent=2))

Ejemplo 04:

.. code:: python

    # Importar la biblioteca requests
    import requests
    import json

    # Realizar una solicitud PUT
    headers = {"accept": "*/*", "Content-Type" : "application/json"}
    data = {'fname': 'Estela', 'lname': "Quiroga"}
    response = requests.put('http://localhost:8000/api/people/Rodriguez', json=data, headers=headers)

    # Obtener el código de estado de la respuesta
    status_code = response.status_code
    data_response = response.json()

    # Imprimir el código de estado de la respuesta
    print()
    print(f"Status code => { status_code}")
    print()
    print(json.dumps(data_response, indent=2))


Ejemplo 04:

.. code:: python

    # Importar la biblioteca requests
    import requests

    # Realizar una solicitud DELETE
    headers = {"accept": "*/*", "Content-Type" : "application/json"}
    response = requests.delete('http://localhost:8000/api/people/Rodriguez', headers=headers)

    # Obtener el código de estado de la respuesta
    status_code = response.status_code

    # Imprimir el código de estado de la respuesta
    print()
    print(f"Status code => { status_code}")
    print()
    print(response.text)


.. code:: python

    # Importar la biblioteca requests
    import requests

    # Realizar una solicitud HEAD
    response = requests.head('https://api.example.com/')

    # Obtener el encabezado de la respuesta
    headers = response.headers

    # Imprimir el encabezado de la respuesta
    print(headers)


.. code:: python

    # Importar la biblioteca requests
    import requests

    # Realizar una solicitud OPTIONS
    response = requests.options('https://api.example.com/')

    # Obtener la información sobre los métodos HTTP admitidos
    allowed_methods = response.headers['Allow']

    # Imprimir la información sobre los métodos HTTP admitidos
    print(allowed_methods)


Estos son solo algunos de los métodos HTTP que se pueden utilizar en las Web APIs. Otros métodos HTTP menos comunes incluyen:

* **TRACE:** Se utiliza para realizar un seguimiento de una solicitud HTTP.
* **CONNECT:** Se utiliza para crear una conexión TCP/IP a un host remoto.
* **OPTIONS:** Se utiliza para obtener información sobre los métodos HTTP admitidos por una API.

La elección del método HTTP correcto para una API depende de la acción que se desee realizar.

**Conclusión**

Las Web APIs son una herramienta poderosa que puede ser utilizada por desarrolladores de todo nivel de experiencia. Las APIs se utilizan para una amplia gama de propósitos y pueden ser una gran manera de mejorar la funcionalidad y la eficiencia de sus aplicaciones web.


**Introducción a Flask, el framework de desarrollo web de Python**

**¿Qué es Flask?**

* Es un microframework ligero y flexible para crear aplicaciones web en Python.
* Es conocido por su simplicidad, naturaleza no opinante y facilidad de uso.
* Proporciona las herramientas esenciales para el desarrollo web, lo que le permite agregar funcionalidad según sea necesario a través de extensiones.

**Características clave:**

* **Minimalista:** No impone mucha estructura, lo que le brinda libertad en las elecciones de diseño.
* **Enrutamiento:** Define patrones de URL para mapear funciones (vistas) que manejan diferentes solicitudes.
* **Plantillas Jinja2:** Utiliza el motor de plantillas Jinja2 para generar contenido HTML dinámico.
* **Biblioteca de utilidades WSGI de Werkzeug:** Construido sobre Werkzeug, que proporciona utilidades WSGI para el manejo de solicitudes y respuestas.
* **Extenso:** Ofrece un rico ecosistema de extensiones (Flask-SQLAlchemy, Flask-Login, etc.) para tareas comunes de desarrollo web.

**Estructura básica:**

1. **Importar Flask:**

.. code:: python

    from flask import Flask

2. **Crear una instancia de la aplicación:**

.. code:: python

    app = Flask(__name__)


3. **Definir rutas:**

.. code:: python

    @app.route('/')
    def index():
        return "Hola, mundo!"


4. **Ejecutar la aplicación:**

.. code:: python

    flask run

**Ventajas de Flask:**

* Simple y fácil de aprender, incluso para principiantes.
* Flexible y adaptable a diversas necesidades de proyectos.
* Gran comunidad y documentación extensa.
* Ideal para prototipado, aplicaciones pequeñas a medianas y API.

**Casos de uso comunes:**

* Sitios web y blogs personales
* API RESTful
* Servicios web
* Plataformas de comercio electrónico
* Paneles de visualización de datos
* Aplicaciones web personalizadas

**Ejemplo básico**

El siguiente ejemplo muestra cómo crear una aplicación web simple con Flask:

.. code: python

    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hola, mundo!"

    if __name__ == '__main__':
        app.run()

Este código crea una aplicación web con una sola ruta, `/`, que devuelve la cadena "Hola, mundo!"

Esto abrirá una instancia de la aplicación en el puerto 5000. Puede acceder a la aplicación en su navegador web en la siguiente URL:

    http://localhost:5000

**Conclusiones**

Flask es un framework de desarrollo web flexible y poderoso que es ideal para una amplia gama de proyectos. Es una buena opción para principiantes y desarrolladores experimentados por igual.

