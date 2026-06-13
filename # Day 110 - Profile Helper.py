# Day 110 - Profile Helper
import json
from pathlib import Path

p = Path("day110_profile.json")
if p.exists():
    data = json.loads(p.read_text())
    print("Loaded name:", data["name"])
    print("Loaded city:", data["city"])
else:
    print("Profile file not found")