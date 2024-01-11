# Clases Decoradoras

class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " fue llamada"
        print(log_string)
        # Abre el fichero de log y escribe
        with open(self._logfile, 'a') as opened_file:
            # Escribimos el contenido
            opened_file.write(log_string + '\n')
        # Enviamos una notificación (ver método)
        self.notify()

        # Devuelve la función base
        return self.func(*args)

    def notify(self):
        # Esta clase simplemente escribe el log, nada más.
        pass

logit._logfile = 'out2.log' # Si queremos usar otro nombre
@logit
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 fue llamada