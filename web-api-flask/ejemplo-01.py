# Importar la biblioteca requests
import requests
import json

# Realizar una solicitud GET
headers = {"accept": "*/*"}
response = requests.get('http://localhost:8000/api/people', headers=headers)

# Obtener el contenido de la respuesta
data = response.json()

# Imprimir el contenido de la respuesta
print(json.dumps(data, indent=2))