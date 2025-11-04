import json

with open('weather.json', 'r', encoding='utf-8') as file:
    weather = json.load(file)

dict = dict()

for weather in weather:
    dict[weather["дата"]] = weather["температура"]

for key, value in dict.items():
    print(key, value)