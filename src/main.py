import requests
import time
import datetime



api_key = '74ff9d00d9d4525dfd3ffbd2cb813111'
base_url = 'http://api.openweathermap.org/data/2.5/onecall/timemachine'

lat = '44.34'
lon = '10.99'

d = datetime.date(2024, 3, 25)
unixtime = time.mktime(d.timetuple())
timestamp = unixtime


response = requests.get(base_url, params={'lat': lat, 'lon': lon, 'dt':timestamp, 'appid': api_key})
weather_data = response.json()

print(weather_data)