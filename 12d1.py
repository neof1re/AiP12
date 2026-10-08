import json
with open("products.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)
for item in data["products"]:
    print(f"Название: {item['name']}")
    print(f"Цена: {item['price']}")
    print(f"Вес: {item['weight']}")
    if item['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()