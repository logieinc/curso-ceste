# Clases Decoradoras
import time

def medir_tiempo_ejecucion(clase):
    class ClaseDecorada(clase):
        def __getattribute__(self, name):
            atributo_original = super().__getattribute__(name)
            if callable(atributo_original):
                def wrapper(*args, **kwargs):
                    inicio = time.time()
                    resultado = atributo_original(*args, **kwargs)
                    fin = time.time()
                    tiempo_ejecucion = fin - inicio
                    print(f"El método '{name}' tomó {tiempo_ejecucion:.5f} segundos en ejecutarse.")
                    return resultado
                return wrapper
            else:
                return atributo_original
    return ClaseDecorada

# Uso del decorador en una clase
@medir_tiempo_ejecucion
class OtraClase:
    def metodo_lento(self):
        time.sleep(2)
        print("¡Método ejecutado!")

# Crear una instancia de la clase decorada
otra_instancia = OtraClase()

# Llamar a un método
otra_instancia.metodo_lento()
