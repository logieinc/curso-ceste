class UtilidadesMatematicas:
    @staticmethod
    def sumar(a, b):
        # Método estático que realiza la suma de dos números
        return a + b

    @staticmethod
    def restar(a, b):
        # Método estático que realiza la resta de dos números
        return a - b

# Uso de los métodos estáticos sin crear una instancia de la clase
resultado_suma = UtilidadesMatematicas.sumar(10, 5)
print(f"Resultado de la suma: {resultado_suma}")

resultado_resta = UtilidadesMatematicas.restar(10, 5)
print(f"Resultado de la resta: {resultado_resta}")
