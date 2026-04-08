#Day 62 - CSV Processing 
import csv

# Write CSV
data = [["Name", "Age"], ["Sai", 23], ["Ram", 25]]
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV created")