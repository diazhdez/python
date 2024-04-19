import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="12345",
        database="escuela"
    )
    if conexion.is_connected():
        print("ELIMINA REGISTRO")
        cursor = conexion.cursor()
        IdAEliminar = input("Introduce el ID del País: ")

        sentencia = """DELETE FROM pais
                        WHERE (paisID= %s)"""
        cursor.execute(sentencia, (IdAEliminar,))
        conexion.commit()
        print("Registro ELIMINADO con éxito...")

except Error as ex:
    print("Error en la conexion de l BD: ", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("La conexión se ha cerrado")
