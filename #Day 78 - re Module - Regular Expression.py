#Day 78 - re Module - Regular Expressions
import re

text = "Contact: alice@python.org or bob@data.com on 2026-04-27"

# Find emails
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print("Emails:", emails)

# Find dates
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
print("Dates:", dates)