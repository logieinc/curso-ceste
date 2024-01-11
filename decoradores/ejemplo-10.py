# Capturando exceptions con decoradores
def capturar_excepcion(metodo):
    def wrapper(*args, **kwargs):
        try:
            return metodo(*args, **kwargs)
        except ZeroDivisionError:
            print("¡Error! División por cero no permitida.")
            return None
        except Exception as e:
            print(f"¡Error inesperado! {type(e).__name__}: {e}")
            return None
    return wrapper

class Calculadora:
    @capturar_excepcion
    def dividir(self, numerador, denominador):
        resultado = numerador / denominador
        return resultado

# Crear una instancia de la clase Calculadora
mi_calculadora = Calculadora()

# Ejemplo de uso del método decorado
resultado_division = mi_calculadora.dividir(10, 2)
print(f"Resultado de la división: {resultado_division}")

# Intentar una división por cero
resultado_division_cero = mi_calculadora.dividir(5, 0)
print(f"Resultado de la división por cero: {resultado_division_cero}")

# Intentar una operación que genere un error inesperado
resultado_error = mi_calculadora.dividir("10", 2)
print(f"Resultado del error: {resultado_error}")
