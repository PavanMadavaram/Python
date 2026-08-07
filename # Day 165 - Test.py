# Day 165 - Test

items = [
    {"done": True},
    {"done": False},
    {"done": True},
]

completed = sum(item["done"] for item in items)

print("Day 165 test:", completed == 2)
print("Day 165 test ok")