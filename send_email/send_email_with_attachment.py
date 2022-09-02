import yagmail
from dotenv import load_dotenv
import os 
import pandas
load_dotenv()

sender = os.getenv('EMAIL')
apppassword = os.getenv('PASSWORD')
yag = yagmail.SMTP(user=sender, password = apppassword)  ### Specify who sends the email and give proper creds

df = pandas.read_csv('contacts.csv') ### Load csv contact list to dataframe

def generate_file(filename, content): ### Function that writes specified content to a file with a particular name (Name_of_mail_receiver.txt)
    with open(filename, 'w') as file:
        file.write(str(content))
        
for index, row in df.itterrows():   ### Go through each row according to indexes
    name = row['name']  ### Extract customer name value from csv
    filename = name + "txt" ### Attachment filename
    amount = row['amount'] ### Extract customer current debt value from csv
    receiver_email = row['email'] ### Extract customer email address value from csv
    
    generate_file(filename,amount)    ### Generate the necessary attachment

    subject = "This is the subject"
    contents = [f"""                    
    Hey {name}, you have to pay {amount}!!
    Bill is attached below.
    """, 'text.txt', filename] ### Send this string, using this file(name)

yag.send(to=sender, subject=subject, contents=contents)  ### Send mail with gmail with content from up above
print("Email sent")
