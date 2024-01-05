# Usando funciones como argumento de otras

def hola():
    return "¡Hola!"

def hazEstoAntesDeHola(func):
    print("Hacer algo antes de llamar a func")
    print(func())


hazEstoAntesDeHola(hola)
# Salida: Hacer algo antes de llamar a func
#        ¡Hola!