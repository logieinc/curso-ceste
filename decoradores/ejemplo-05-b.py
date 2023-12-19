# Tu primer decorador

@nuevo_decorador
def funcion_a_decorar():
    print("Soy la función que necesita ser decorada")

funcion_a_decorar()
# Salida: Haciendo algo antes de llamar a a_func()
#        Soy la función que necesita ser decorada
#        Haciendo algo después de llamar a a_func()

# El uso de @nuevo_decorador es simplemente una forma acortada
# de hacer lo siguiente.
funcion_a_decorar = nuevo_decorador(funcion_a_decorar)