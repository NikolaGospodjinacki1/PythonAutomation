from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(input_currency, output_currency):
    url = f"https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find("span", class_="ccOutputRslt").get_text()
    rate = float(rate[:-4])
    
    return rate


### Name is now equal to filename ###
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Currency Rate APi</h1> <p>Example URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    rate= get_currency(in_cur, out_cur)
    result_dictionary = {'input_currency': in_cur, 'output_currency': out_cur, 'rate': rate}
    return jsonify(result_dictionary)


app.run()