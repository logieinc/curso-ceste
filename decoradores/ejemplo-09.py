# Apilando decoradores, decorador 1: Convertir el resultado a mayúsculas

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
print()
print(resultado_final)
