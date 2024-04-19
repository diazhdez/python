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
        print('Conexión Exitosa')
        InfoServer = connection.get_server_info()
        print('Información del servidor:', InfoServer)

except Error as ex:
    print("Error durante la conexión:", ex)

finally:
    if connection.is_connected():
        connection.close()
        print('La conexión ha finalizado')
