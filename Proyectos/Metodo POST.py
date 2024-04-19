import requests

# URL de ejemplo para la solicitud POST
url = 'https://www.ejemplo.com/api/post_endpoint'

# Datos que deseas enviar en la solicitud POST (en este caso, un diccionario)
data = {
    'nombre': 'Josue',
    'edad': 19
}

# Realiza la solicitud POST con los datos
response = requests.post(url, data=data)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Imprime el contenido de la respuesta
    print("Contenido de la respuesta:")
    print(response.text)
else:
    print('Error en la solicitud. Código de estado: {response.status_code}')
