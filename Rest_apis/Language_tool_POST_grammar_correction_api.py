import requests
import json

url = 'https://api.languagetool.org/v2/check'
data = {
    'text': 'Tis is a nixe day!',
    'language' : 'auto'
}

response = requests.post(url, data=data)
result = json.loads(response.text)
result_final = json.dumps(result, indent=2)


print(result_final)