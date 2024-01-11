# Tu primer decorador
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
funcion_a_decorar()