Decoradores
----------

Los decoradores son funciones que modifican la funcionalidad de otras funciones, y ayudan a hacer nuestro código más corto y Pytónico o Pythonic.
A continuación veremos lo que son, cómo se crean y cómo podemos usarlos.

Todo es un objeto en Python:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
    #Salida: NameError

    print(saluda())
    #Salida: 'Hola Ceste'


Definir funciones dentro de funciones:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En Python podemos definir funciones dentro de otras funciones veamos el siguiente ejemplo:

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

    saluda()
    #Saluda: NameError: name 'saluda' is not defined

Ya hemos visto entonces como podemos definir funciones dentro de otras funciones. En otras palabras, podemos crear funciones anidadas. Pero para entender bien los decoradores, necesitamos ir un paso más allá. Las funciones también pueden devolver otras funciones.


Devolviendo funciones desde funciones:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

No es necesario ejecutar una función dentro de otra. Simplemente podemos devolverla como salida:

.. code:: python

    def hola(nombre="Covadonga"):
        def saluda():
            return "Estás dentro de la función saluda()"

        def bienvenida():
            return "Estás dentro de la función bienvenida()"

        if nombre == "Covadonga":
            return saluda
        else:
            return bienvenida

    a = hola()
    print(a)
    #Salida: <function saluda at 0x7f2143c01500>

    #Es decir, la variable 'a' ahora apunta a la función
    # saluda() declarada dentro de hola(). Por lo tanto podemos llamarla.

    print(a())
    #Salida: Estás dentro de la función saluda()

Echa un vistazo otra vez al código. Si te fijas en el if/else, estamos devolviendo ``saluda`` y ``bienvenida`` y no ``saluda()`` y ``bienvenida()``. ¿A qué se debe esto? Se debe a que cuando usas paréntesis ``()`` la función se ejecuta. Por lo contrario, si no los usas la función es pasada y puede ser asignada a una variable sin ser ejecutada.

Vamos a analizar el código paso por paso. Al principio usamos ``a = hola()``, por lo que el parámetro para ``nombre`` que se toma es Covadonga ya que es el que hemos asignado por defecto. Esto hará que en el ``if`` se entre en ``nombre == "Covadonga"``, lo que hará que se devuelva la función saluda. Si por lo contrario hacemos la llamada a la función con ``a = hola(nombre="Pelayo")``, la función devuelta será ``bienvenida``.


