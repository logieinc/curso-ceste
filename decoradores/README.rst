Devolviendo funciones desde funciones:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

