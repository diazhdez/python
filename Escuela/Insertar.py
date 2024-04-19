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
        print('Insertando Datos')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM pais;")
        cursor.fetchall()
        idSiguiente = cursor.rowcount+1
        print('Ultimo ID:', idSiguiente)
        # Solicita los nuevos datos
        nombreNuevo = input('Introduce el nommbre del nuevo País: ')
        siglasNuevas = input('Introduce las siglas: ')

        sentencia = """INSERT INTO pais (paisID, paisNombre, paisSigla)
                    VALUES ('{0}', '{1}', '{2}')""".format(idSiguiente, nombreNuevo, siglasNuevas)
        cursor.execute(sentencia)
        connection.commit()
        print('Registro Insertado...')

except Error as ex:
    print("Error durante la conexión:", ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conexión ha finalizado')
