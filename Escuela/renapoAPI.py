import requests

url = "https://apimarket.mx/api/renapo/grupo/obtener-curp"

payload = {
    'nombres': 'Angeles Natividad',
    'paterno': 'Ramirez',
    'materno': 'Vazquez',
    'diaNacimiento': '23',
    'mesNacimiento': '04',
    'anoNacimiento': '2004',
    'claveEntidad': '12',
    'sexo': 'M'
}
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer a7efb401-789a-47b7-b75d-1c5711cad7f6'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
