# Day 90 - Test
import json

sample = '{"title": "Test", "body": "OK"}'
data = json.loads(sample)
print("News test:", data["title"] == "Test")
print("Day 90 test ok")