import json

utf8 = [chr(i) for i in range(0x10000)]


def get_new_key(key, exist_key):
    if key in exist_key:
        return exist_key[key]
    else:
        new_key = utf8[len(exist_key)]
    exist_key[key] = new_key
    return new_key


def rename_keys_recursively(data, exist_key):
    if isinstance(data, dict):
        new_dict = {}
        for key, value in data.items():
            new_key = get_new_key(key, exist_key)
            new_dict[new_key] = rename_keys_recursively(value, exist_key)
        return new_dict
    elif isinstance(data, list):
        return [rename_keys_recursively(item, exist_key) for item in data]
    else:
        return data


def compressed(filename):
    with open('input.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    key_mapping = dict()
    transformed_data = dict()
    transformed_data["value"] = rename_keys_recursively(data, key_mapping)
    transformed_data["key"] = key_mapping

    with open('compressed.json', 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, ensure_ascii=False, indent=2)


def decompressed(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

    keys = data['key']
    reversed_keys = dict()
    for key, value in keys.items():
        reversed_keys[value] = key

    value = data['value']
    transformed_data = rename_keys_recursively(value, reversed_keys)

    with open('decompressed.json', 'w', encoding='utf-8') as f:
        json.dump(transformed_data, f, ensure_ascii=False, indent=2)


compressed('input.json')
decompressed('compressed.json')
