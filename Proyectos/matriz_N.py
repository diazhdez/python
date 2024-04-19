import random
# Josué Díaz Hernández 4ª "A" TICS

# Tamaño de la matriz (N x N)
N = int(input('Taño de la matriz: '))

# Crear una matriz vacía
matriz = []

# Llenar la matriz con números enteros aleatorios
for i in range(N):
    fila = []
    for i in range(N):
        numero_entero = random.randint(1, 100)
        fila.append(numero_entero)
    matriz.append(fila)

# Imprimir la matriz
for fila in matriz:
    print(fila)