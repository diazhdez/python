import funciones

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tabla = int(input('Ingrese un número a multiplicar: '))

for numero in numeros:
    resultado = funciones.multiplicar(numero, tabla)
    print(resultado)
