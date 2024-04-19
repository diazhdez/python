import funciones

operacion = input('Tipo de operación a resolver: ')
primero = int(input('Primer valor: '))
segundo = int(input('Segundo valor: '))

match operacion:
    case 'suma':
        print(funciones.sumar(primero, segundo))
    case 'resta':
        print(funciones.restar(primero, segundo))
    case 'multiplicacion':
        print(funciones.multiplicar(primero, segundo))
    case 'divicion':
        print(funciones.dividir(primero, segundo))
