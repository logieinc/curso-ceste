# Importar la biblioteca requests
import requests
import json

# Realizar una solicitud PUT
headers = {"accept": "*/*", "Content-Type" : "application/json"}
data = {'fname': 'Estela', 'lname': "Quiroga"}
response = requests.put('http://localhost:8000/api/people/Rodriguez', json=data, headers=headers)

# Obtener el código de estado de la respuesta
status_code = response.status_code
data_response = response.json()

# Imprimir el código de estado de la respuesta
print()
print(f"Status code => { status_code}")
print()
print(json.dumps(data_response, indent=2))