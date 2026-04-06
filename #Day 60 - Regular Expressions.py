#Day 60 - Regular Expressions 
import re

email = "sai@example.com"
if re.match(r"[^@]+@[^@]+\.[^@]+", email):
    print("Valid email")
else:
    print("Invalid email")