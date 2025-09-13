import json

student_info = {
    "имя": "Иван Иванов",
    "возраст": 20,
    "оценки": [4, 5, 4, 3, 5]
}

json_data = json.dumps(student_info, ensure_ascii=False, indent=2)
print(json_data)