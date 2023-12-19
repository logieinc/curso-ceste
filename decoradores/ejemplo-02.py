# Definir funciones dentro de funciones

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
# Salida:Estas dentro de la función hola()
#       Estás dentro de la función saluda()
#       Estás dentro de la función bienvenida()
#       De vuelta a la función hola()

# Esto muestra como cada vez que llamas a la función hola()
# se llama en realidad también a saluda() y bienvenida()
# Sin embargo estas dos últimas funciones no están accesibles
# fuera de hola(). Si lo intentamos, tendremos un error.

saluda()
#Saluda: NameError: name 'saluda' is not defined


