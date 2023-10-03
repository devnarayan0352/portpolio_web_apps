import smtplib , ssl
import os




def send_email(user_email, message):
    host = "smtp.gmail.com"
    port = 465
    username = "devnarayan0352@gmail.com"
    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()
    receiver = user_email

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
