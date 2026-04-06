#Day 60 - Regex Helper
import re

text = "Phone: 123-456-7890"
phone = re.search(r"\d{3}-\d{3}-\d{4}", text)
if phone:
    print("Phone found:", phone.group())