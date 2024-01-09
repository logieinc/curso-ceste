# Tu primer decorador

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