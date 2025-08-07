inventory = {
    "apple": {"price": 1.5, "category": "fruit"},
    "banana": {"price": 0.75, "category": "fruit"},
    "milk": {"price": 2.99, "category": "dairy"},
    "bread": {"price": 3.25, "category": "bakery"},
    "cheese": {"price": 4.5, "category": "dairy"},
    "chocolate": {"price": 2.25, "category": "snacks"}
}

cart = ["apple", "milk", "bread", "cheese", "chocolate", "banana", "banana"]

total = 0
categories = set()
most_expensive_item = None
highest_price = 0

quantities = {}

for item in cart:
    
    quantities[item] = (current := quantities.get(item, 0)) + 1

print("🧾 RECEIPT")
print("-" * 30)
for item, qty in quantities.items():
    details = inventory[item]
    line_total = details["price"] * qty
    total += line_total

    categories.add(details["category"])

    
    if (price := details["price"]) > highest_price:
        highest_price = price
        most_expensive_item = item

    print(f"{item.capitalize():<12} x{qty:<2} @ ${details['price']:.2f} = ${line_total:.2f}")

print("-" * 30)
print(f"Total:           ${total:.2f}")
print(f"Unique categories: {', '.join(sorted(categories))}")
print(f"Most expensive item: {most_expensive_item.capitalize()} (${highest_price:.2f})")
