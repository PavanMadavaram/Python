# Day 174 - Habit Streak Tracker

days = [
    {"day": 171, "completed": True},
    {"day": 172, "completed": True},
    {"day": 173, "completed": True},
    {"day": 174, "completed": True},
]

streak = 0

for entry in days:
    if entry["completed"]:
        streak += 1
    else:
        streak = 0

    status = "✅ complete" if entry["completed"] else "❌ missed"
    print(f"Day {entry['day']}: {status}")

print("Current streak:", streak)