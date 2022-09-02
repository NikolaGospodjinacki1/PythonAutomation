import yagmail
from dotenv import load_dotenv
import os 
import time
from datetime import datetime as dt
load_dotenv()


receiver = 'sasanih223@seinfaq.com'

subject = "Test subject 123"

contents = """
here is the mail!
Is it working?
"""
while True:
    now = dt.now()
    if now.hour == 13 and now.minute == 15: 
        yag = yagmail.SMTP(user=os.getenv('EMAIL'), password = os.getenv('PASSWORD'))
        yag.send(to=receiver, subject=subject, contents=contents)
        print("Email sent")
        time.sleep(60)
 ### YOU CAN ALSO USE PYTHON ANYWHERE TO SCHEDULE YOUR EMAILS ###
 ###  https://pythonhow.com/how/schedule-a-python-script-for-execution-at-a-specific-time-every-day/ ###