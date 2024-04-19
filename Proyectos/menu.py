def mostrar_menu():
    print('''Menu 
    1. Insertar  Nodo
    2. Buscar Nodo
    3. Eliminar Nodo
    4. Imprimir Lista
    5. Tamaño de Lista
    6. Ordenar Lista
    7. Salir''')

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Opción 1: Insertar  Nodo")
    elif opcion == "2":
        print("Opción 2: Buscar Nodo")
    elif opcion == "3":
        print("Opción 3: Eliminar Nodo")
    elif opcion == "4":
        print("Opción 4: Imprimir Lista")
    elif opcion == "5":
        print("Opción 5: Tamaño de Lista")
    elif opcion == "6":
        print("Opción 6: Ordenar Lista")
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
