import json

with open('dataForModificate.json', 'r', encoding='utf-8') as file:
    student = json.load(file)

student['email'] = 'email'

with open('dataForModificate.json', 'w', encoding='utf-8') as file:
    json.dump(student, file, indent=4 , ensure_ascii=False)
