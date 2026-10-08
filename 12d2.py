import json
with open("products.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)
name = input("Введите название нового продукта: ")
price = int(input("Введите цену: "))
weight = int(input("Введите вес (в граммах): "))
available_input = input("Продукт в наличии? (да/нет): ").lower()
available = True if available_input == "да" else False
new_product = {
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
}
data["products"].append(new_product)
with open("products.json", mode="w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
print("\n--- Обновленный список продуктов ---\n")
for item in data["products"]:
    print(f"Название: {item['name']}")
    print(f"Цена: {item['price']}")
    print(f"Вес: {item['weight']}")
    if item['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()