# Day 10 - Nested Lists (PURE PYTHON ONLY)
shopping_list = [
    ["Rice", 80, 5],
    ["Dal", 120, 2],
    ["Oil", 150, 1],
    ["Milk", 60, 3]
]

print("🛒 Hyderabad Grocery Bill")
total = 0

for item in shopping_list:
    name = item[0]
    price_per_kg = item[1]
    kg = item[2]
    cost = price_per_kg * kg
    total = total + cost
    print(name + ": " + str(kg) + "kg × ₹" + str(price_per_kg) + " = ₹" + str(cost))

print("Total bill: ₹" + str(total))
print("Day 10 complete - Pure Python!")
