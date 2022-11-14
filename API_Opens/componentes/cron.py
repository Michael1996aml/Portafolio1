import imaplib
import email
from email.header import decode_header
from db import *
from machine import *

def Automatizacion():
    username = 'portafolio.duocuc.2022@gmail.com'
    password = 'mzfzqybucciwgmou'
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(username, password)
    status, mensajes = imap.select("INBOX")
    N = 2
    mensajes = int(mensajes[0])
    data = []
    for i in range(mensajes, mensajes - N, -1):
        temp=[]
        try:
            res, mensaje = imap.fetch(str(i), "(RFC822)")
        except:
            break
        for respuesta in mensaje:
            if isinstance(respuesta, tuple):
                mensaje = email.message_from_bytes(respuesta[1])
                subject = decode_header(mensaje["Subject"])[0][0]
                if isinstance(subject, bytes):
                    subject = subject.decode()
                from_ = mensaje.get("From")
                if mensaje.is_multipart():
                    for part in mensaje.walk():
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            body = part.get_payload(decode=True).decode()
                            body_depurado = body.replace(","," ")
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            temp.append(from_)
                            temp.append(mensaje["Date"])
                            temp.append(subject)
                            temp.append(body)
        data.append(temp)
    valor = []
    plantilla = consulta_plantilla()
    for i in range(len(data)):
            cuerpo = data[i][3]
            valor = data[i]
            clasificado = clasificar(correo = cuerpo)
            valor.append(clasificado)
            for i in range(len(valor)):
                nombre = valor[0]
                if valor[i] == 'Despido':
                    asunto = plantilla[1]
                    cuerpo = plantilla[2]
                    Enviar_Email(nombre = nombre,cuerpo = cuerpo, asunto = asunto)
            migracion_datos(datos = valor)
    imap.close()
    imap.logout()

Automatizacion()
