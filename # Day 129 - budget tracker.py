# Day 129 - budget tracker
from dataclasses import dataclass

@dataclass
class Expense:
    item: str
    amount: float

expenses = [
    Expense("Rent", 1200.00),
    Expense("Groceries", 240.50),
    Expense("Internet", 59.99),
    Expense("Transport", 85.25),
]

total = sum(e.amount for e in expenses)

for e in expenses:
    print(f"{e.item}: {e.amount}")

print("Total:", round(total, 2))