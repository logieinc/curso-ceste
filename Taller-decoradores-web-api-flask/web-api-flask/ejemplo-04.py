# Importar la biblioteca requests
import requests

# Realizar una solicitud DELETE
headers = {"accept": "*/*", "Content-Type" : "application/json"}

response = requests.delete('http://localhost:8000/api/people/Rodriguez', headers=headers)

# Obtener el código de estado de la respuesta
status_code = response.status_code

# Imprimir el código de estado de la respuesta
print()
print(f"Status code => { status_code}")
print()
print(response.text)