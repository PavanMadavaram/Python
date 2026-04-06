#Day 61 - JSON Helper
import json

# JSON string to Python
json_data = '{"city": "Hyderabad", "experience": 1}'
python_dict = json.loads(json_data)
print("City:", python_dict["city"])