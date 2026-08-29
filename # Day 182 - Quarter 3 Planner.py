# Day 182 - Quarter 3 Planner

quarter_goals = [
    {"topic": "Data structures & algorithms", "priority": "high", "hours": 20},
    {"topic": "Web scraping & API integration", "priority": "high", "hours": 15},
    {"topic": "Automation scripts", "priority": "medium", "hours": 10},
    {"topic": "Unit testing & documentation", "priority": "medium", "hours": 8},
]

total_hours = sum(goal["hours"] for goal in quarter_goals)

print("🎯 Q3 Study & Project Plan (Day 182/365)\n")
for goal in quarter_goals:
    print(f"• {goal['topic']} [{goal['priority']}] — {goal['hours']}h")

print(f"\nTotal planned investment: {total_hours} hours")