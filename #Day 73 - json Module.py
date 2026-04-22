#Day 73 - json Module 
import json

data = {"name": "User", "score": 100}
json_str = json.dumps(data)
print("JSON:", json_str)

parsed = json.loads(json_str)
print("Parsed:", parsed["name"])