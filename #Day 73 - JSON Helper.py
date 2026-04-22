#Day 73 - JSON Helper 
import json
import os

data = {"name": "Python", "day": 73, "complete": True}

# Write JSON file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=4)

# Read back
if os.path.exists('data.json'):
    with open('data.json', 'r') as f:
        loaded = json.load(f)
    print("Loaded:", loaded["name"])
else:
    print("File not created")