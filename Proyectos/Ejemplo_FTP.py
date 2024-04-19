from ftplib import FTP

# Configura la conexión FTP
ftp = FTP('ftp.example.com')  # Reemplaza 'ftp.example.com' con la dirección de tu servidor FTP
ftp.login(user='tu_usuario', passwd='tu_contraseña')  # Reemplaza 'tu_usuario' y 'tu_contraseña'

# Lista los archivos en el directorio remoto
ftp.dir()

# Sube un archivo al servidor
with open('archivo_local.txt', 'rb') as archivo_local:
    ftp.storbinary('STOR archivo_remoto.txt', archivo_local)

# Descarga un archivo del servidor
with open('archivo_descargado.txt', 'wb') as archivo_descargado:
    ftp.retrbinary('RETR archivo_remoto.txt', archivo_descargado.write)

# Cierra la conexión FTP
ftp.quit()