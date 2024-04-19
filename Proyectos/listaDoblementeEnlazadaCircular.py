# Primero vamos a crear una clase llamada NodoDoble
# la cual representa un nodo de una lista doblemente enlazada circular.
class NodoDoble:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Cada nodo tiene tres atributos: data para almacenar datos, next para apuntar al siguiente nodo y prev para apuntar al nodo anterior.

# Ahora vamos a definir una clase llamada ListaDoblementeEnlazadaCircular, que representa la lista doblemente enlazada circular.


class ListaDoblementeEnlazadaCircular:
    # En el método __init__ de la clase ListaDoblementeEnlazadaCircular,
    # se inicializa head como None, lo que indica que la lista está vacía en el momento de la creación.
    def __init__(self):
        self.head = None

    #  El método insertar_nodo permite agregar un nuevo nodo con un valor data al final de la lista.
    def insertar_nodo(self, data):
        nuevo_nodo = NodoDoble(data)
        # Si la lista está vacía se crea un nuevo nodo que se enlaza consigo mismo.
        if self.head is None:
            self.head = nuevo_nodo
            nuevo_nodo.next = nuevo_nodo
            nuevo_nodo.prev = nuevo_nodo
        # Si la lista no está vacía, se agrega el nuevo nodo al final de la lista.
        else:
            tail = self.head.prev
            tail.next = nuevo_nodo
            nuevo_nodo.prev = tail
            nuevo_nodo.next = self.head
            self.head.prev = nuevo_nodo
    # El método buscar_nodo busca un nodo con un valor específico en la lista.
    # Comienza desde head y recorre la lista en un bucle, comparando el valor de data en cada nodo.

    def buscar_nodo(self, data):
        if self.head is None:
            return False

        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:
                break
        return False
    # El método eliminar_nodo elimina un nodo con un valor específico de la lista.
    # Comienza desde head y recorre la lista en busca del nodo con el valor dado.

    def eliminar_nodo(self, data):
        if self.head is None:
            return

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break
    # El método imprimir_lista imprime los valores de todos los nodos en la lista,
    # comenzando desde head y siguiendo los punteros next hasta regresar al nodo head.

    def imprimir_lista(self):
        if self.head is None:
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print()
    # El método borrar_lista simplemente establece head como None, lo que vacía la lista.

    def borrar_lista(self):
        self.head = None


def menu():
    print('''1. Insertar nodo 
    2. Buscar nodo
    3. Eliminar nodo
    4. Imprimir lista
    5. Borrar lista
    6. Salir''')


# Después se crea una instancia de la clase ListaDoblementeEnlazadaCircular llamada lista_doble_circular.
lista_doble_circular = ListaDoblementeEnlazadaCircular()

# Y se  entra en un bucle while que muestra el menú al usuario y permite que el usuario seleccione una opción del mismo.
while True:
    menu()
    opcion = int(input("Selecciona una opción: "))

    # Usando la expresión match, se procesa la opción seleccionada por el usuario y se ejecuta la función correspondiente.
    match opcion:
        case 1:
            valor = int(input("Ingresa el valor del nodo a insertar: "))
            lista_doble_circular.insertar_nodo(valor)
            print("Valor Insertado Exitosamente.")
        case 2:
            valor = int(input("Ingresa el valor del nodo a buscar: "))
            if lista_doble_circular.buscar_nodo(valor):
                print("El nodo está en la lista.")
            else:
                print("El nodo no está en la lista.")
        case 3:
            valor = int(input("Ingresa el valor del nodo a eliminar: "))
            lista_doble_circular.eliminar_nodo(valor)
            print("Valor Eliminado Exitosamente.")
        case 4:
            print("----------------------------")
            lista_doble_circular.imprimir_lista()
            print("----------------------------")
        case 5:
            lista_doble_circular.borrar_lista()
            print("Lista borrada.")
        case 6:
            break
        case _:
            print("Opción no válida. Por favor, selecciona una opción válida.")
        # El bucle continúa hasta que el usuario seleccione la opción de Salir, en cuyo caso el bucle se rompe y el programa termina.