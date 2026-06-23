# Day 120 - Todo Helper
import json
from pathlib import Path

p = Path("day120_todos.json")
if p.exists():
    data = json.loads(p.read_text())
    for item in data:
        status = "Done" if item["done"] else "Pending"
        print(f"{item['title']} - {status}")
else:
    print("No todo file found")