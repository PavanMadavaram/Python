# Day 182 - Test

def filter_by_priority(goals, priority_level="high"):
    return [g for g in goals if g.get("priority") == priority_level]


test_goals = [
    {"name": "A", "priority": "high"},
    {"name": "B", "priority": "low"},
    {"name": "C", "priority": "high"},
]

high_prio = filter_by_priority(test_goals, "high")

print("Day 182 test:", len(high_prio) == 2)
print("Day 182 test ok")