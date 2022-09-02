import smtplib ## standard python lib
from email.mime.text import MIMEText ### needed for fancy mails
from email.mime.multipart import MIMEMultipart

sender = "hotmail/outlook.com"
receiver = "whatever@gmail.com"
password = 'storesafelyin.env'

message = MIMEMultipart() ### dict with different fields for different parts of an email
message['From'] = sender
message['To'] = receiver
message['Subject'] = "hello again!" ### subject is always a string
body = """
<h2> Hi there! </h2>
There are onlytwo cats flying today!
Let's hope for more!
"""
mimetext = MIMEText(body, 'html') ### convert body to html processed mimetext thing
message.attach(body) ### add body to your message

### use outlook smtp servers ( you need a domain and a port )
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls() ### protocol for securely sending emails
server.login(sender, password) ### logins into your hotmail/outlook account
message_string =message.as_string() ### convert dict to string because sendmail wants a string
server.sendmail(sender, receiver, message_string)
server.quit() ### logs out of your account

### NEW ACCOUNT EMAILS END UP IN THE SPAM FOLDER ###
### YOU NEED TO VERIFY YOUR OUTLOOK/HOTMAIL ACCOUNT when sending mail programmatically or you might get a SMTPDataError or something similar)