import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def enviar_email():

    smtp_ssl_host = 'mail.xxxxxxx.es' 
    smtp_ssl_port = 465
    username = 'xxxxxx' 
    password = 'xxxxxxx'
    sender =  'direccionenvio@gmail.es' 

    target = 'destino@gmail.com'


    ruta_adjunto = 'fichero.xlsx'
    nombre_adjunto = 'fichero.xlsx'

    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    
    # Establecemos los atributos del mensaje
    mensaje['From'] = sender
    #mensaje['To'] = ", ".join(targets)
    mensaje['Subject'] = 'CONSUMO ACUMULADO'
    cuerpo = 'Envio de datos de consumo acumulado' 
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open('fichero.xlsx', 'rb')
    
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)


    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
    server.login(username, password)
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()

    # Enviamos el mensaje
    server.sendmail(sender,target, texto)

    # Cerramos la conexión
    server.quit()


