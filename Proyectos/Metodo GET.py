import requests

# URL de ejemplo
url = 'https://www.google.com/'

# Realizar una solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Imprimir el contenido de la respuesta
    print("Contenido de la respuesta:")
    print(response.text)
else:
    print('Error en la solicitud. Código de estado: {response.status_code}')