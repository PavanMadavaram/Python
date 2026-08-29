# Day 182 - Planner Helper

def filter_by_priority(goals, priority_level="high"):
    return [g for g in goals if g.get("priority") == priority_level]


plan = [
    {"topic": "DSA", "priority": "high"},
    {"topic": "APIs", "priority": "high"},
    {"topic": "Testing", "priority": "medium"},
]

print("High priority focus areas:")
for item in filter_by_priority(plan, "high"):
    print(f" - {item['topic']}")