# Wraps  & Decoradores con argumentos

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
