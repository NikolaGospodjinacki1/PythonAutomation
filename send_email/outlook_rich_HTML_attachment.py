from email.mime.base import MIMEBase
import smtplib ## standard python lib
from email.mime.text import MIMEText ### needed for fancy mails
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
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

attachment_path = 'tiger.jpeg'
attachment_file = open(attachment_path, 'rb') ### gets path and creates a file object
payload = MIMEBase('application', 'octate-stream') ### protocols that you need 
payload.set_payload(attachment_file.read()) ### add file CONTENTS to the payload (that's why you need to use read)
payload.add_header('Content-Disposition', 'attachment', filename=attachment_path) ### use this path(this file) as an attachment
message.attach(payload) ### finally add the payload to the message
server = smtplib.SMTP('smtp.office365.com', 587) ### use outlook smtp servers ( you need a domain and a port )
server.starttls() ### protocol for securely sending emails
server.login(sender, password) ### logins into your hotmail/outlook account
message_string =message.as_string() ### convert dict to string because sendmail wants a string
server.sendmail(sender, receiver, message_string)
server.quit() ### logs out of your account

### NEW ACCOUNT EMAILS END UP IN THE SPAM FOLDER ###
### YOU NEED TO VERIFY YOUR OUTLOOK/HOTMAIL ACCOUNT when sending mail programmatically or you might get a SMTPDataError or something similar)