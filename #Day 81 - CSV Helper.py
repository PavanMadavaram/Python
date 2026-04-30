#Day 81 - CSV Helper
import csv

# Read CSV
with open('users.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} from {row['City']}")
