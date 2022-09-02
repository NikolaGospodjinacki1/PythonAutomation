import requests

url = "https://cgi-lib.berkley.edu/ex/fup.cgi"

file = open('myfile.txt', 'rb')

req = requests.post(url, files={"upfile":file})

print(req.text)