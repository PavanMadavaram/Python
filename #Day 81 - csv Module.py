#Day 81 - csv Module 
import csv

# Write CSV
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'Hyderabad'],
    ['Bob', 25, 'Bangalore']
]

with open('users.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("users.csv created!")