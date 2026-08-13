# Day 168 - expense summary

expenses = [
    {"category": "Food", "amount": 250},
    {"category": "Transport", "amount": 120},
    {"category": "Books", "amount": 300},
    {"category": "Food", "amount": 180},
]

totals = {}

for expense in expenses:
    category = expense["category"]
    totals[category] = totals.get(category, 0) + expense["amount"]

for category, total in totals.items():
    print(f"{category}: ₹{total}")

print("Grand total:", sum(totals.values()))