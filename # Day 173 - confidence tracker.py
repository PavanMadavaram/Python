# Day 173 - confidence tracker

areas = [
    {"name": "Python basics", "score": 7},
    {"name": "Problem solving", "score": 6},
    {"name": "Project work", "score": 8},
    {"name": "Consistency", "score": 9},
]

average = sum(area["score"] for area in areas) / len(areas)

for area in areas:
    print(f"{area['name']}: {area['score']}/10")

print(f"Average confidence: {average:.1f}/10")