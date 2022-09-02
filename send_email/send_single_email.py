import yagmail
from dotenv import load_dotenv
import os 
## import time
load_dotenv()


receiver = 'sasanih223@seinfaq.com'

subject = "Test subject 123"

contents = """
here is the mail!
Is it working?
"""
## while True:
yag = yagmail.SMTP(user=os.getenv('EMAIL'), password = os.getenv('PASSWORD'))
yag.send(to=receiver, subject=subject, contents=contents)
print("Email sent")
#time.sleep(360)
