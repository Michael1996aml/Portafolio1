#pip install -U scikit-learn scipy matplotlib
import smtplib,ssl
from email.message import EmailMessage
import joblib

def clasificar(correo):
    data = [correo]
    vector = joblib.load('vectorizer.joblib')
    clasificador = joblib.load('SVC.joblib')
    data = vector.transform(data)
    valor = clasificador.predict(data)
    return valor

def Enviar_Email(nombre, cuerpo, asunto):
        email_sender = 'portafolio.duocuc.2022@gmail.com'
        email_password = 'mzfzqybucciwgmou'
        email_receiver = nombre

        subject = asunto
        body = cuerpo

        em =EmailMessage()
        em['front'] = email_sender
        em ['to'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver, em.as_string())
