def hola(nombre="Ceste"):
    return "Hola " + nombre

print(hola())
# Salida: 'Hola Ceste'

# Podemos asignar una función a una variable
saluda = hola
# No usamos () porque no la estamos llamando, sino que la estamos
# asignado a una variable

print(saluda())
# Salida: 'Hola Ceste'

# También podemos eliminar la función asignada a la variable con del
try:
    del hola
    print(hola())
except Exception as e:
    print('Ocurrió un Exception. {}'.format(e.args[-1]))
#Salida: NameError

print(saluda())
#Salida: 'Hola Ceste'