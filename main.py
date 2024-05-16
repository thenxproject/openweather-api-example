import sys

import requests
import json

API_KEY = sys.argv[1]

params = {
    "lat": 44.819430,
    "lon": -93.316870,
    "units": "imperial",
    #"lat": 39.9042,
    #"lon": 116.4074,
    #"units": "metric",
    "appid": API_KEY,
    "lang": "en"
}


# https://api.openweathermap.org/data/2.5/weather
# https://api.openweathermap.org/data/3.0/onecall

api_response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
data = api_response.json()

print(f"""The forcast for today in {data["name"]} is:""")
print(f"""{data["weather"][0]["description"]}""")
print(f"""The temperature is {data["main"]["temp"]}°F""")
print(f"""The wind speed is {data["wind"]["speed"]} mph""")

print("")
print("Full data:")
print(json.dumps(data, indent=4))

