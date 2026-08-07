# Day 165 - reading progress tracker

readings = [
    {"title": "Morning reading", "minutes": 20, "completed": True},
    {"title": "Notes and reflection", "minutes": 10, "completed": True},
    {"title": "Evening review", "minutes": 15, "completed": False},
]

completed = sum(item["completed"] for item in readings)
total_minutes = sum(item["minutes"] for item in readings)

for item in readings:
    status = "Done" if item["completed"] else "Pending"
    print(f"{item['title']}: {status}")

print(f"Completed: {completed}/{len(readings)}")
print(f"Planned time: {total_minutes} minutes")