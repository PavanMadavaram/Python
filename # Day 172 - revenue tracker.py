# Day 172 - revenue tracker

transactions = [
    {"customer": "Asha", "amount": 1200, "status": "paid"},
    {"customer": "Ravi", "amount": 800, "status": "paid"},
    {"customer": "Mina", "amount": 500, "status": "pending"},
    {"customer": "Kiran", "amount": 1500, "status": "paid"},
]

paid = [t for t in transactions if t["status"] == "paid"]
revenue = sum(t["amount"] for t in paid)

for transaction in transactions:
    print(
        f"{transaction['customer']}: "
        f"₹{transaction['amount']} - {transaction['status']}"
    )

print("Paid transactions:", len(paid))
print("Total revenue:", f"₹{revenue}")