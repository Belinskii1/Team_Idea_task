import requests
from pprint import pprint
from datetime import datetime, timezone

API_KEY = '38ad86acd1e942701713eb98c83f7a21'  # введите свой ключ

# задание 3.а. 2.
my_toun = 'Moskow'  #  введите название своего города
country_code =  '643'  #  введите код в формате ISO 3166
response = requests.get(
    f'http://api.openweathermap.org/geo/1.0/direct?q={my_toun},{country_code}&limit=1&appid={API_KEY}'
)
response = response.json()
response = response[0]

lat = response['lat']
lon = response['lon']

response_5_days = requests.get(
    f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
)
response_5_days = response_5_days.json()

sunrise = response_5_days['city']['sunrise'] # время восхода солнца
sunset = response_5_days['city']['sunset'] # время заката солнца
sunrise = datetime.fromtimestamp(sunrise, tz=timezone.utc)
sunset = datetime.fromtimestamp(sunset, tz=timezone.utc)

day_duration = sunset - sunrise

print(day_duration) # разницу за 5 дней нашел только в платной pro версии в разрезе 30 дней


# задание 3.а. 1.

pprint(response_5_days['list'][0]['main']['feels_like'])

result_list = []
result_dict = {}
for i in range(5):
    result = int(
        response_5_days['list'][i]['main']['feels_like']
        - response_5_days['list'][i]['main']['temp']
    )
    day = response_5_days['list'][i]['dt']
    day = str(datetime.fromtimestamp(day, tz=timezone.utc))
    result_dict[day]=result

print(min(result_dict.keys())) # день с минимальной разницей ощущений темп.
