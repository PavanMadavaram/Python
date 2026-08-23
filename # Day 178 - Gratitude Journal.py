# Day 178 - Gratitude Journal

entries = [
    {"day": 175, "note": "Finished a tough coding challenge"},
    {"day": 176, "note": "Learned a new Python concept"},
    {"day": 177, "note": "Stayed consistent with practice"},
    {"day": 178, "note": "Helped someone with their code"},
]

for entry in entries:
    print(f"Day {entry['day']}: {entry['note']}")

print(f"\nTotal entries: {len(entries)}")