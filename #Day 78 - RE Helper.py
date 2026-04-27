#Day 78 - RE Helper
import re

# Validate phone
phone_pattern = r'^\+91-\d{10}$'
phone = '+91-9876543210'
match = re.match(phone_pattern, phone)
print("Valid phone?", bool(match))

# Replace
text = "Hello 123 World 456"
clean = re.sub(r'\d+', '', text)
print("Clean text:", clean)