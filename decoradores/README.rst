Decoradores
----------

`Curso gráfico MIRO <https://miro.com/welcomeonboard/M2owWWFuRHBwaXJxbm1rR2pnWjdvazdBZ2l1ZUdWVU1taTAxWExqNDdyd1Q0d2htMGszSEw1TWJ3ZU90dVpZVnwzNDU4NzY0NTY3ODY3MjMyMTY2fDI=?share_link_id=544290942241>`__

Los decoradores son funciones que modifican la funcionalidad de otras funciones, y ayudan a hacer nuestro código más corto y Pytónico o Pythonic (forma de escribir código en Python que sigue los principios y las convenciones de diseño que son típicos y aceptados en la comunidad de programadores de Python).

Es importante aclarar que los decoradores forman parte de un `patrón de diseño de software <https://refactoring.guru/es/design-patterns/decorator>`__, entendiendo la frase "patrón de diseño" se refiere a soluciones generales y reutilizables para problemas comunes en el diseño de software.

¿Por qué los decoradores son importantes en Python?:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Los decoradores juegan un papel crucial en la programación en Python por varias razones:

A - Reutilización del código:
Los decoradores permiten separar las preocupaciones transversales, como el registro, la validación, la autenticación o el almacenamiento en caché, de la lógica central de las funciones o clases. Esto favorece la reutilización del código y la modularidad.

B - Facilidad de lectura y mantenimiento:
Los decoradores proporcionan una forma limpia y concisa de añadir funcionalidad al código existente sin saturar la implementación original. Mejoran la legibilidad del código aislando comportamientos específicos y facilitando su comprensión y mantenimiento.

C - Metaprogramación y extensibilidad:
Los decoradores permiten la modificación dinámica del código en tiempo de ejecución, lo que posibilita técnicas avanzadas de metaprogramación. Proporcionan un mecanismo flexible para ampliar y personalizar el comportamiento de funciones o clases sin modificar su definición original.

A continuación veremos lo que son, cómo se crean y cómo podemos usarlos.

Todo es un objeto en Python:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ejemplo 01:

.. code:: python

    def hola(nombre="Ceste"):
        return "Hola " + nombre

    print(hola())
    # Salida: 'Hola Ceste'

    # Podemos asignar una función a una variable
    saluda = hola
    # No usamos () porque no la estamos llamando, sino que la estamos
    # asignado a una variable

    print(saluda())
    # Salida: 'Hola Ceste'

    # También podemos eliminar la función asignada a la variable con del
    try:
        del hola
        print(hola())
    except Exception as e:
        print('Ocurrió un Exception. {}'.format(e.args[-1]))
    # Salida: NameError

    print(saluda())
    # Salida: 'Hola Ceste'


Definir funciones dentro de funciones:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En Python podemos definir funciones dentro de otras funciones veamos el siguiente ejemplo:

Ejemplo 02:

.. code:: python

    def hola(nombre="Ceste"):
        print("Estás dentro de la función hola()")

        def saluda():
            return "Estás dentro de la función saluda()"

        def bienvenida():
            return "Estás dentro de la función bienvenida()"

        print(saluda())
        print(bienvenida())
        print("De vuelta a la función hola()")

    hola()
    #Salida:Estas dentro de la función hola()
    #       Estás dentro de la función saluda()
    #       Estás dentro de la función bienvenida()
    #       De vuelta a la función hola()

    # Esto muestra como cada vez que llamas a la función hola()
    # se llama en realidad también a saluda() y bienvenida()
    # Sin embargo estas dos últimas funciones no están accesibles
    # fuera de hola(). Si lo intentamos, tendremos un error.
    try:
        saluda()
    except Exception as e:
        print('Ocurrió un Exception. {}'.format(e.args[-1]))
    #Saluda: NameError: name 'saluda' is not defined

Ya hemos visto entonces como podemos definir funciones dentro de otras funciones. En otras palabras, podemos crear funciones anidadas. Pero para entender bien los decoradores, necesitamos ir un paso más allá. Las funciones también pueden devolver otras funciones.

Devolviendo funciones desde funciones:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No es necesario ejecutar una función dentro de otra. Simplemente podemos devolverla como salida:

Ejemplo 03:

.. code:: python

    def hola(nombre="Ceste"):
        def saluda():
            return "Estás dentro de la función saluda()"

        def bienvenida():
            return "Estás dentro de la función bienvenida()"

        if nombre == "Ceste":
            return saluda
        else:
            return bienvenida

    a = hola()
    print(a)
    #Salida: <function saluda at 0x...>

    #Es decir, la variable 'a' ahora apunta a la función
    # saluda() declarada dentro de hola(). Por lo tanto podemos llamarla.

    print(a())
    #Salida: Estás dentro de la función saluda()

Echa un vistazo otra vez al código.
Si te fijas en el if/else, estamos devolviendo ``saluda`` y ``bienvenida`` y no ``saluda()`` y ``bienvenida()``. ¿A qué se debe esto? Se debe a que cuando usas paréntesis ``()`` la función se ejecuta. Por lo contrario, si no los usas la función es pasada y puede ser asignada a una variable sin ser ejecutada.

Vamos a analizar el código paso por paso.
Al principio usamos ``a = hola()``, por lo que el parámetro para ``nombre`` que se toma es "Ceste" ya que es el que hemos asignado por defecto. Esto hará que en el ``if`` se entre en ``nombre == "Ceste"``, lo que hará que se devuelva la función saluda. Si por lo contrario hacemos la llamada a la función con ``a = hola(nombre="Pelayo")``, la función devuelta será ``bienvenida``.


Usando funciones como argumento de otras:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Por último, podemos hacer que una función tenga a otra como entrada y que además la ejecute dentro de sí misma. En el siguiente ejemplo podemos ver como ``hazEstoAntesDeHola()`` es una función que de alguna forma encapsula a la función que se le pase como parámetro, añadiendo una determinada funcionalidad. En este ejemplo simplemente imprimimos algo por pantalla antes de llamar a la función.

Ejemplo 04:

.. code:: python

    def hola():
        return "¡Hola!"

    def hazEstoAntesDeHola(func):
        print("Hacer algo antes de llamar a func")
        print(func())

    hazEstoAntesDeHola(hola)
    #Salida: Hacer algo antes de llamar a func
    #        ¡Hola!


Ahora ya tienes todas las piezas del rompecabezas. Los decoradores son funciones que decoran a otras funciones, pudiendo ejecutar código antes y después de la función que está siendo decorada.

Tu primer decorador:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Realmente en el ejemplo anterior ya vimos como crear un decorador. Vamos a modificarlo y hacerlo más realista.

Ejemplo 05-a:

.. code:: python

    def nuevo_decorador(a_func):

        def envuelveLaFuncion():
            print("Haciendo algo antes de llamar a a_func()")

            a_func()

            print("Haciendo algo después de llamar a a_func()")

        return envuelveLaFuncion

    def funcion_a_decorar():
        print("Soy la función que necesita ser decorada")

    funcion_a_decorar()
    #Salida: "Soy la función que necesita ser decorada"

    funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
    #Ahora funcion_a_decorar está envuelta con el decorador que hemos creado

    funcion_a_decorar()
    #Salida: Haciendo algo antes de llamar a a_func()
    #        Soy la función que necesita ser decorada
    #        Haciendo algo después de llamar a a_func()

Simplemente hemos aplicado todo lo aprendido en los apartados anteriores. Así es exactamente como funcionan los decoradores en Python. Envuelven una función para modificar su comportamiento de una manera determinada.

Lo que nos debe quedar claro es que al momento de implementar un decorador estaremos trabajando, con por lo menos, 3 funciones. El input, el output y la función principal. Para que nos quede más en claro a mi me gusta nombrar a las funciones como: A, B, y C.

Donde A recibe como parámetro B para dar como salida a C. Esta es una pequeña "formula" la cual me gusta mucho mencionar.

    A(B) -> C

Tal vez te preguntes ahora porqué no hemos usado @ en el código. Esto es debido a que @ es simplemente una forma de hacerlo más corto, pero ambas opciones son perfectamente válidas.

Python nos da una forma de arreglar este problema usando ``functools.wraps``

Ejemplo 05-b:

.. code:: python

    from functools import wraps

    def nuevo_decorador(a_func):
        @wraps(a_func)
        def envuelveLaFuncion():
            print("Haciendo algo antes de llamar a a_func()")
            a_func()
            print("Haciendo algo después de llamar a a_func()")
        return envuelveLaFuncion

    @nuevo_decorador
    def funcion_a_decorar():
        print("Soy la función que necesita ser decorada")

    print(funcion_a_decorar.__name__)
    # Salida: funcion_a_decorar

Veamos variante al codigo anteriormente citado.

Ejemplo 05-c:

.. code:: python

    from functools import wraps

    def nombre_decorador(f):
        @wraps(f)
        def decorada(*args, **kwargs):
            if not can_run:
                return "La función no se ejecutará"
            return f(*args, **kwargs)
        return decorada

    @nombre_decorador
    def func():
        return("La función se esta ejecutando")

    can_run = True
    print(func())
    # Salida: La función se esta ejecutando

    can_run = False
    print(func())
    # Salida: La función no se ejecutará

Nota: ``@wraps`` toma una función para ser decorada y añade la funcionalidad de copiar el nombre de la función, el *docstring*, los argumentos y otros parámetros asociados. Esto nos permite acceder a los elementos de la función a decorar una vez decorada. Es decir, resuelve el problema que vimos con anterioridad.


Wraps & Decoradores con argumentos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hemos visto ya el uso de ``@wraps``, y tal vez te preguntes ¿pero no es también un decorador? De hecho si te fijas acepta un parámetro (que en nuestro caso es una función). A continuación te explicamos como crear un decorador que también acepta parámetros de entrada.

@wraps es un decorador en Python que se utiliza para preservar la información de la función original cuando se aplica otro decorador a esa función. Esto es especialmente útil cuando estás creando decoradores personalizados y quieres asegurarte de que la función decorada conserve su nombre, su documentación y otros metadatos importantes.

Cuando aplicas un decorador a una función sin usar @wraps, a menudo pierdes información sobre la función original. @wraps resuelve este problema al copiar los metadatos de la función original al decorador.

Ejemplo 06:

.. code:: python

    from functools import wraps

    def mi_decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Ejecutando {func.__name__} con argumentos: {args} y kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} ha terminado")
            return result
        return wrapper

    @mi_decorador
    def funcion_con_argumentos(a, b):
        """Esta es la documentación de funcion_con_argumentos."""
        print(f"Suma de {a} y {b}: {a + b}")

    # Probemos acceder a algunos metadatos de la función original
    print(f"Nombre de la función decorada: {funcion_con_argumentos.__name__}")
    print(f"Documentación de la función decorada: {funcion_con_argumentos.__doc__}")

    # Llamamos a la función decorada
    funcion_con_argumentos(3, 5)


Anidando un Decorador dentro de una Función
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Puedes anidar un decorador dentro de una función, lo cual puede ser útil para personalizar el comportamiento del decorador basado en ciertos parámetros locales. Aquí tienes un ejemplo:

Ejemplo 07:

.. code:: python

    from functools import wraps

    def logit(logfile='out.log'):
        def logging_decorator(func):
            @wraps(func)
            def wrapped_function(*args, **kwargs):
                log_string = func.__name__ + " fue llamada"
                print(log_string)
                # Abre el fichero y añade su contenido
                with open(logfile, 'a') as opened_file:
                    # Escribimos en el fichero el contenido
                    opened_file.write(log_string + '\n')
                return func(*args, **kwargs)
            return wrapped_function
        return logging_decorator

    @logit()
    def myfunc1():
        pass

    myfunc1()
    # Salida: myfunc1 fue llamada
    # Se ha creado un fichero con el nombre por defecto (out.log)

    @logit(logfile='func2.log')
    def myfunc2():
        pass

    myfunc2()
    # Salida: myfunc2  fue llamada
    # Se crea un fichero func2.log

Clases Decoradoras
~~~~~~~~~~~~~~~~~

Siguiendo la linea de decoradores, ya en el caso anterior decorador sobre funciones, también podemos aplicarlo a las clases en python

Decorar una clase en Python conlleva varias ventajas, similar a decorar funciones. Aquí hay algunas ventajas específicas al decorar clases:

Reutilización de Código:
    Puedes aplicar un decorador a múltiples clases, lo que permite la reutilización del código y la consistencia en el comportamiento decorado.

Separación de Preocupaciones:
    Los decoradores permiten separar las preocupaciones relacionadas con la funcionalidad específica del código de la lógica principal de la clase.

    La Separación de Preocupaciones (SoC, por sus siglas en inglés "Separation of Concerns") es un principio de diseño de software que aboga por dividir un programa en componentes distintos, cada uno de los cuales se ocupa de una preocupación o responsabilidad específica. Este enfoque facilita la comprensión, el mantenimiento y la modificación del código, ya que cada componente se centra en una tarea clara y separada

Añadir Comportamiento sin Modificar el Código Fuente:
    Puedes agregar funcionalidades adicionales a una clase sin modificar directamente su código fuente. Esto es útil cuando no tienes control sobre la implementación de la clase o cuando deseas mantener un código limpio y modular.

Mejora de la Legibilidad:
    Los decoradores pueden mejorar la legibilidad del código al encapsular aspectos específicos del comportamiento de la clase en funciones separadas. Esto facilita la comprensión del propósito de cada parte del código.

Extensibilidad:
    Los decoradores ofrecen una forma flexible de extender el comportamiento de una clase. Puedes crear nuevos decoradores y aplicarlos según sea necesario sin modificar la clase original.

Mejora de la Mantenibilidad:
    Al separar las responsabilidades y mantener una estructura modular, el código decorado tiende a ser más fácil de mantener y modificar sin afectar otras partes del sistema.

Logging y Depuración:
    Puedes utilizar decoradores para agregar lógica de registro (logging) o funciones de depuración a los métodos de una clase sin afectar la implementación original. Esto facilita la identificación y solución de problemas.

Aplicación Selectiva de Comportamientos:
    Los decoradores permiten aplicar selectivamente ciertos comportamientos a instancias específicas de una clase o a todas las instancias, según sea necesario.

En resumen, decorar clases en Python proporciona una forma elegante y poderosa de extender y modificar el comportamiento de las clases sin cambiar su código fuente, lo que contribuye a la modularidad y la legibilidad del código.

Ejemplo 08-a:

.. code:: python

    def mi_decorador(clase):
        class ClaseDecorada(clase):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.nueva_atributo = 42

            def nuevo_metodo(self):
                print("¡Este es un nuevo método!")

        return ClaseDecorada

    @mi_decorador
    class MiClaseOriginal:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def imprimir(self):
            print(f"x: {self.x}, y: {self.y}")

    # Creamos una instancia de la clase decorada
    objeto_decorado = MiClaseOriginal(x=1, y=2)
    objeto_decorado.imprimir()  # Método original de la clase
    objeto_decorado.nuevo_metodo()  # Método agregado por el decorador
    print(objeto_decorado.nueva_atributo)  # Atributo agregado por el decorador

Ejemplo 08:

.. code:: python

    import time

    def medir_tiempo_ejecucion(clase):
        class ClaseDecorada(clase):
            def __getattribute__(self, name):
                atributo_original = super().__getattribute__(name)
                if callable(atributo_original):
                    def wrapper(*args, **kwargs):
                        inicio = time.time()
                        resultado = atributo_original(*args, **kwargs)
                        fin = time.time()
                        tiempo_ejecucion = fin - inicio
                        print(f"El método '{name}' tomó {tiempo_ejecucion:.5f} segundos en ejecutarse.")
                        return resultado
                    return wrapper
                else:
                    return atributo_original

        return ClaseDecorada

    # Uso del decorador en una clase
    @medir_tiempo_ejecucion
    class OtraClase:
        def metodo_lento(self):
            time.sleep(2)
            print("¡Método ejecutado!")

    # Crear una instancia de la clase decorada
    otra_instancia = OtraClase()

    # Llamar a un método
    otra_instancia.metodo_lento()


Apilando decoradores
~~~~~~~~~~~~~~~~~

En Python, es posible apilar varios decoradores sobre una misma función. La apilación de decoradores significa que puedes aplicar más de un decorador a una función, en el orden en que se colocan. Cada decorador modifica o agrega comportamiento a la función de manera acumulativa.

Aquí tienes un ejemplo de cómo puedes usar decoradores apilados:

En este ejemplo, los decoradores se aplican en el orden inverso al que aparecen. La función saludar primero pasa a través del decorador convertir_mayusculas, luego por agregar_prefijo y, finalmente, por invertir_resultado. Puedes experimentar con el orden de los decoradores según tus necesidades y el efecto que desees lograr.

La apilación de decoradores es una técnica poderosa y flexible en Python que permite componer funciones con diferentes funcionalidades de manera modular.

Ejemplo 09:

.. code:: python

    def convertir_mayusculas(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado.upper()
        return wrapper

    # Decorador 2: Agregar un prefijo al resultado
    def agregar_prefijo(prefijo):
        def decorador(func):
            def wrapper(*args, **kwargs):
                resultado = func(*args, **kwargs)
                return f"{prefijo} {resultado}"
            return wrapper
        return decorador

    # Decorador 3: Invertir el resultado
    def invertir_resultado(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado[::-1]
        return wrapper

    # Apilación de decoradores
    @invertir_resultado
    @agregar_prefijo("Resultado:")
    @convertir_mayusculas
    def saludar(nombre):
        return f"Hola, {nombre}!"

    # Llamada a la función decorada
    resultado_final = saludar("John")

    # Resultado
    print(resultado_final)

Decoradores integrados
~~~~~~~~~~~~~~~~~

Python incluye algunos decoradores integrados que proporcionan funcionalidades específicas. Aquí hay algunos de los decoradores incorporados más comunes en Python:

@property:
Utilizado para convertir un método en una propiedad. Permite el acceso a un método como si fuera un atributo, sin necesidad de llamarlo como una función.

.. code:: python

    class MiClase:
        def __init__(self):
            self._x = 0

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, valor):
            self._x = valor

.. code:: python

    class Circulo:
        def __init__(self, radio):
            self._radio = radio

        @property
        def radio(self):
            return self._radio

        @property
        def area(self):
            return 3.14 * self._radio**2

        @property
        def diametro(self):
            return 2 * self._radio

    # Crear una instancia de la clase Circulo
    mi_circulo = Circulo(radio=5)

    # Acceder a la propiedad 'radio' como si fuera un atributo
    print(f"Radio del círculo: {mi_circulo.radio}")

    # Acceder a la propiedad 'area' (calculada) como si fuera un atributo
    print(f"Área del círculo: {mi_circulo.area}")

    # Acceder a la propiedad 'diametro' (calculada) como si fuera un atributo
    print(f"Diametro del círculo: {mi_circulo.diametro}")


@classmethod:
Indica que un método de clase debe ser llamado en lugar de un método de instancia. Recibe la clase como primer argumento en lugar de la instancia.

.. code:: python

    class MiClase:
        contador = 0

        def __init__(self):
            MiClase.contador += 1

        @classmethod
        def obtener_contador(cls):
            return cls.contador

.. code:: python

    class Persona:
        contador_personas = 0

        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
            Persona.contador_personas += 1

        @classmethod
        def crear_persona(cls, nombre, edad):
            # Utiliza el constructor de clase para crear una nueva instancia de Persona
            return cls(nombre, edad)

        @classmethod
        def obtener_contador(cls):
            # Accede a un atributo de clase desde el método de clase
            return cls.contador_personas

    # Crear una persona usando el método de clase
    nueva_persona = Persona.crear_persona("Juan", 25)

    # Acceder a los atributos de la persona creada
    print(f"Nombre: {nueva_persona.nombre}, Edad: {nueva_persona.edad}")

    # Obtener el contador de personas utilizando el método de clase
    contador_actual = Persona.obtener_contador()
    print(f"Número total de personas: {contador_actual}")


@staticmethod:
Indica que un método no depende del estado de la instancia ni de la clase y, por lo tanto, no recibe la instancia o la clase como primer argumento.

.. code:: python

    class Utilidades:
        @staticmethod
        def sumar(a, b):
            return a + b

.. code:: python

    class UtilidadesMatematicas:
        @staticmethod
        def sumar(a, b):
            # Método estático que realiza la suma de dos números
            return a + b

        @staticmethod
        def restar(a, b):
            # Método estático que realiza la resta de dos números
            return a - b

    # Uso de los métodos estáticos sin crear una instancia de la clase
    resultado_suma = UtilidadesMatematicas.sumar(10, 5)
    print(f"Resultado de la suma: {resultado_suma}")

    resultado_resta = UtilidadesMatematicas.restar(10, 5)
    print(f"Resultado de la resta: {resultado_resta}")



classmethod vs @staticmethod:
@classmethod y @staticmethod son decoradores relacionados pero tienen diferencias en la forma en que manejan los argumentos. @classmethod recibe la clase como primer argumento, mientras que @staticmethod no recibe ni la instancia ni la clase automáticamente.

.. code:: python

    class Ejemplo:
        @classmethod
        def metodo_clase(cls, arg1, arg2):
            # cls es la clase
            pass

        @staticmethod
        def metodo_estatico(arg1, arg2):
            # No se pasa la clase automáticamente
            pass

Capturando exceptions con decoradores
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Puedes usar decoradores para capturar excepciones en los métodos de una clase. Aquí hay un ejemplo de cómo hacerlo:

Ejemplo 10:

.. code:: python

    def capturar_excepcion(metodo):
        def wrapper(*args, **kwargs):
            try:
                return metodo(*args, **kwargs)
            except ZeroDivisionError:
                print("¡Error! División por cero no permitida.")
                return None
            except Exception as e:
                print(f"¡Error inesperado! {type(e).__name__}: {e}")
                return None
        return wrapper

    class Calculadora:
        @capturar_excepcion
        def dividir(self, numerador, denominador):
            resultado = numerador / denominador
            return resultado

    # Crear una instancia de la clase Calculadora
    mi_calculadora = Calculadora()

    # Ejemplo de uso del método decorado
    resultado_division = mi_calculadora.dividir(10, 2)
    print(f"Resultado de la división: {resultado_division}")

    # Intentar una división por cero
    resultado_division_cero = mi_calculadora.dividir(5, 0)
    print(f"Resultado de la división por cero: {resultado_division_cero}")

    # Intentar una operación que genere un error inesperado
    resultado_error = mi_calculadora.dividir("10", 2)
    print(f"Resultado del error: {resultado_error}")


En este ejemplo, el decorador capturar_excepcion envuelve el método dividir de la clase Calculadora. Este decorador intenta ejecutar el método y captura cualquier excepción especificada en los bloques except. Si ocurre una excepción, se imprime un mensaje adecuado y se devuelve None.

Al aplicar el decorador @capturar_excepcion al método dividir, estás agregando la funcionalidad de manejo de excepciones al método sin modificar su código interno.

