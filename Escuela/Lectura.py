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
        print('Consultando datos de País')
        cursor = connection.cursor()
        cursor.execute("SELECT database();")
        baseDatos = cursor.fetchone()
        print('La base de datos es:', baseDatos)
        cursor.execute('SELECT * FROM pais;')
        registros = cursor.fetchall()
        for fila in registros:
            print(fila[0], fila[1], fila[2])
        print('Total de registro:', cursor.rowcount)

except Error as ex:
    print("Error durante la conexión:", ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conexión ha finalizado')
