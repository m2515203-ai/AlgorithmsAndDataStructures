import json


def is_instance_klass(class_name, value):
    return isinstance(value, getattr(__builtins__, class_name))


def validate(data: dict, validate_dict: dict):
    errors = []

    for key, value in validate_dict.items():
        if value["required"] and key not in data:
            errors.append(f"Field \"{key}\" is required but not provided")
            continue
        if not is_instance_klass(value["class"], data[key]):
            errors.append(
                f"Field \"{key}\" is not correct type, required {value['class']} but actual {data[key].__class__}")
            continue
        if isinstance(validate_dict[key], dict) and validate_dict[key].get("values", False):
            errors.append(validate(data[key], value["values"]))

    return errors


def validate_json_file(file_path):
    global f, data, template
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open("template.json", 'r', encoding='utf-8') as f:
        template = json.load(f)
    return validate(data, template)


error = validate_json_file("data_correct.json")
# [[], []]
print(error)

error = validate_json_file("data_incorrect.json")
# ['Field "user" is not correct type, required dict but actual <class \'str\'>',
# ['Field "name" is not correct type, required str but actual <class \'int\'>',
#  'Field "citizens" is required but not provided']]
print(error)
