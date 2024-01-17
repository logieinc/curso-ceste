def mi_decorador(clase):
    class ClaseDecorada(clase):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.nueva_atributo = 42

        def nuevo_metodo(self):
            print("¡Este es un nuevo método!")

    return ClaseDecorada

@mi_decorador
class MiClaseOriginal:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"x: {self.x}, y: {self.y}")

# Creamos una instancia de la clase decorada
objeto_decorado = MiClaseOriginal(x=1, y=2)
objeto_decorado.imprimir()  # Método original de la clase
objeto_decorado.nuevo_metodo()  # Método agregado por el decorador
print(objeto_decorado.nueva_atributo)  # Atributo agregado por el decorador
