# Day 183 - DSA Practice Tracker

topics = [
    {"topic": "Arrays & Strings", "problems_solved": 12, "status": "completed"},
    {"topic": "Hash Maps & Sets", "problems_solved": 8, "status": "in progress"},
    {"topic": "Two Pointers", "problems_solved": 5, "status": "in progress"},
    {"topic": "Stacks & Queues", "problems_solved": 0, "status": "planned"},
]

total_solved = sum(item["problems_solved"] for item in topics)

print("📚 Daily Data Structures & Algorithms Roadmap (Day 183/365)\n")
for item in topics:
    badge = "✅" if item["status"] == "completed" else "⏳"
    print(f"{badge} {item['topic']}: {item['problems_solved']} problems [{item['status']}]")

print(f"\nTotal problems solved: {total_solved}")