import smtplib,ssl
import socket

# on rentre les renseignements pris sur le site du fournisseur
smtp_address = 'smtp.gmail.com'
smtp_port = 465

# on rentre les informations sur notre adresse e-mail
email_address = 'raspberry.fablab70300@gmail.com'
email_password = 'passiflore00'

# on rentre les informations sur le destinataire
email_receiver = 'raspberry.fablab@gmail.com'

# on crée la connexion
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
  # connexion au compte
  server.login(email_address, email_password)
  # envoi du mail
  print('ozhjey(y"')
  for i in range(5):
    server.sendmail(email_address, email_receiver, 'Subject : truc muche{} \n\n essai n{}  \nhttps://fablab3lapins.org/'.format(i,i))