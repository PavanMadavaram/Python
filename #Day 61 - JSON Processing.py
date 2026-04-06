#Day 61 - JSON Processing 
import json

# Python dict to JSON
data = {"name": "Sai", "skills": ["Python", "Data Analysis"]}
json_str = json.dumps(data, indent=2)
print("JSON:", json_str)