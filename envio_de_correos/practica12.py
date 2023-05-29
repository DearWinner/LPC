import smtplib
#Aaron Avila Mata 1998679 Grupo:062
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# Datos del remitente
correo_remitente = 'aaronavilamata0@gmail.com'
clave_remitente = ''
# Datos del destinatario
correo_destinatario = ' gerardo.bernal@uanl.edu.mx'
# Configuración del mensaje
mensaje = MIMEMultipart()
mensaje['From'] = correo_remitente
mensaje['To'] = correo_destinatario
mensaje['Subject'] = 'Correo de prueba con imagen adjunta'
# Cuerpo del correo en formato HTML
cuerpo = """
<html>
  <head></head> Practica 12
  <body>
    <p>Alumno: Aaron Avila Mata Matricula:1998679.</p>
    <p><img src="cid:image1"></p>
  </body>
</html>
"""
# Adjuntar el cuerpo del correo en formato HTML
mensaje.attach(MIMEText(cuerpo, 'html'))
# Adjuntar la imagen
with open('fcfm_cool.png', 'rb') as archivo_imagen:
    imagen = MIMEImage(archivo_imagen.read())
    imagen.add_header('Content-ID', '<image1>')
    mensaje.attach(imagen)
# Conexión al servidor SMTP
servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
servidor_smtp.starttls()
# Inicio de sesión en el servidor SMTP
servidor_smtp.login(correo_remitente, clave_remitente)
# Envío del correo electrónico
servidor_smtp.sendmail(correo_remitente, correo_destinatario, mensaje.as_string())

# Cierre de sesión en el servidor SMTP
servidor_smtp.quit()
