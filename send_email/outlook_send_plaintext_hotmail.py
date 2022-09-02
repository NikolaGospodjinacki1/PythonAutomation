import smtplib ## standard python lib

sender = "hotmail/outlook.com"
receiver = "whatever@gmail.com"
password = 'storesafelyin.env'

message = """\
Subject: Sample subject

This is Nikola!
Just wanted to say hi :)
"""  ### no fonts no attachments, empty line after subject

### use outlook smtp servers ( you need a domain and a port )
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls() ### protocol for securely sending emails
server.login(sender, password) ### logins into your hotmail/outlook account
server.sendmail(sender, receiver, message)
server.quit() ### logs out of your account

### NEW ACCOUNT EMAILS END UP IN THE SPAM FOLDER ###