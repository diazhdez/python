def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    izquierda = []
    derecha = []
    for i in range(1, len(lista)):
        izquierda.append(lista[i]) if lista[i] < pivote else derecha.append(lista[i])

    return quicksort(izquierda) + [pivote] + quicksort(derecha)


numeros = [23, 45, 16, 37, 3, 99, 22]
ordenados = quicksort(numeros)
print(ordenados)
