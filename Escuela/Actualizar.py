import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='12345',
        database='escuela'
    )

    if connection.is_connected():
        print('Actualizar Datos')
        cursor = connection.cursor()
        actualizarNombre = input('Introduce el nuevo nombre del Pais: ')
        actualizarSiglas = input('Introduce las nuevas siglas del Pais: ')
        buscarID = input('Introduce el ID a buscar: ')
        sentencia = """UPDATE pais
                        SET paisNombre = %s,
                            paisSigla = %s
                        WHERE paisID = %s;"""
        cursor.execute(sentencia, (actualizarNombre, actualizarSiglas, buscarID))

        # sentencia = """UPDATE pais
        #                 SET paisNombre = %s,
        #                     paisSigla = %s
        #                 WHERE paisID = ('{0}');""".format(buscarID)
        # cursor.execute(sentencia, (actualizarNombre, actualizarSiglas))
        
        # sentencia = """UPDATE pais
        #                 SET paisNombre = ('{0}'),
        #                     paisSigla = ('{1}')
        #                 WHERE paisID = ('{2}');""".format(actualizarNombre, actualizarSiglas, buscarID)
        # cursor.execute(sentencia)
        connection.commit()
        print('Registro actualizado con éxito...')


except Error as ex:
    print("Error durante la conexión:", ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conexión ha finalizado')
