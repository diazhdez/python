lista = []

cantidad = int(input('Ingrese la cantidad de elementos en la lista: '))

i = 0

while i < cantidad:
    print('Ingrese el elemento', i+1,':')
    nom = input()
    lista.append(nom)
    i += 1

lista.sort()
print(lista)
