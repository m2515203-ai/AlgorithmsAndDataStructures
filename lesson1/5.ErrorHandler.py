import json


def safe_read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return {"success": True, "data": data}
    except FileNotFoundError as e:
        return {"error": "Некоректный путь", "details": str(e)}
    except json.JSONDecodeError as e:
        return {"error": "Некорректный JSON-формат", "details": str(e)}
    except UnicodeDecodeError:
        return {"error": "Проблема с кодировкой файла"}
    except Exception as e:
        return {"error": f"Неизвестная ошибка: {str(e)}"}


result = safe_read_json("data.json")

if result.get("success"):
    print("Данные успешно загружены:")
    print(json.dumps(result["data"], ensure_ascii=False, indent=2))
else:
    print(f"Ошибка: {result.get('error', 'Неизвестная ошибка')}")
    if "details" in result:
        print(f"Подробности: {result['details']}")
