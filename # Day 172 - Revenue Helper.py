# Day 172 - Revenue Helper

transactions = [
    {"amount": 100, "status": "paid"},
    {"amount": 250, "status": "pending"},
    {"amount": 400, "status": "paid"},
]

paid_total = sum(
    item["amount"]
    for item in transactions
    if item["status"] == "paid"
)

print("Paid total:", paid_total)