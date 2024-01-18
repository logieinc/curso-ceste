# Importar la biblioteca requests
import requests
import json

# Importar la biblioteca requests
import requests
import json

# Realizar una solicitud GET
headers = {"accept": "*/*", "Content-Type" : "application/json"}

response = requests.get('http://localhost:8000/api/people/Perez', headers=headers)

# Obtener el código de estado de la respuesta
status_code = response.status_code
data_response = response.json()

# Imprimir el código de estado de la respuesta
print()
print(f"Status code => { status_code}")
print()
print(json.dumps(data_response, indent=2))