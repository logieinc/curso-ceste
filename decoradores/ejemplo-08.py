# Decoradores con argumentos

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