import yagmail
from dotenv import load_dotenv
import os 
import pandas as pd
## import time
load_dotenv()


receiver = 'sasanih223@seinfaq.com'

subject = "Test subject 123"



dataframe = pd.read_csv("contacts.csv")

for index, row in dataframe.interrows():
    contents = f"""
    Hi {row['name']}, here is the mail!
    Is it working?
    """
    yag = yagmail.SMTP(user=os.getenv('EMAIL'), password = os.getenv('PASSWORD'))
    yag.send(to=row['email'], subject=subject, contents=contents)
    print("Email sent")
#time.sleep(360)