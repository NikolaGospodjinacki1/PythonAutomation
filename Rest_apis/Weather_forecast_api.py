
import requests

def get_weather(city_name,units="metric", API_key="88628e0b6b0d982999a96c2130b76be4"):
    url= f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units={units}"
    r = requests.get(url)
    raw = r.json()
    with open("weather_data.txt", 'a') as f:
        for dicty in raw['list']:
            f.write(f"{raw['city']['name']},{dicty['dt_txt']},{dicty['main']['temp']},{dicty['weather'][0]['description']}\n")
    print("Done with gathering data")


get_weather(city_name="Belgrade")
    

    