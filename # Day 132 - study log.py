# Day 132 - study log
from datetime import datetime

entries = [
    ("Read", "2 Samuel 14"),
    ("Reflect", "Forgiveness matters"),
    ("Write", "Key takeaway notes"),
]

for action, detail in entries:
    print(f"{action}: {detail}")
print("Logged at:", datetime.now().strftime("%Y-%m-%d %H:%M"))