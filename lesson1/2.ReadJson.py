import json

with open('data.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

print(students['name'])