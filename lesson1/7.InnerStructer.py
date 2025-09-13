import json


def find_by_name(json_data, name):
    for category, subcategories in catalog.items():
        for subcategory, products in subcategories.items():
            for product in products:
                if product["name"] == name:
                    return product
    return None


with open('catalog.json', 'r', encoding='utf-8') as file:
    catalog = json.load(file)


product = find_by_name(catalog,"iPhone 15")
print(product)

