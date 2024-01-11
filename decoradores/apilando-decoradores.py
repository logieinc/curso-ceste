# Decorador 1: Convertir el resultado a mayúsculas

'''
En Python, es posible apilar varios decoradores sobre una misma función. La apilación de decoradores significa que puedes aplicar más de un decorador a una función, en el orden en que se colocan. Cada decorador modifica o agrega comportamiento a la función de manera acumulativa.

Aquí tienes un ejemplo de cómo puedes usar decoradores apilados:

En este ejemplo, los decoradores se aplican en el orden inverso al que aparecen. La función saludar primero pasa a través del decorador convertir_mayusculas, luego por agregar_prefijo y, finalmente, por invertir_resultado. Puedes experimentar con el orden de los decoradores según tus necesidades y el efecto que desees lograr.

La apilación de decoradores es una técnica poderosa y flexible en Python que permite componer funciones con diferentes funcionalidades de manera modular.

'''


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
