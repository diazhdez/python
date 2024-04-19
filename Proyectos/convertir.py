temperatura = float(input('Ingrese la temperatura: '))

escala = input(
    'Ingrese la escala de medición: Fahrenheit (F) o Celsius (C): ').upper()

if escala == 'F':
    celsius = (temperatura - 32) * 5/9
    print('Temperatura a grados Celsius: {}'.format(celsius))
elif escala == 'C':
    fahrenheit = temperatura * 1.8 + 32
    print('Temperatura a grados Fahrenheit: {}'.format(fahrenheit))
else:
    print('Escala incorrecta')
