#Day 98 - pathlib + CSV combo
from pathlib import Path
import csv

data = [
    ["name", "score"],
    ["Asha", 91],
    ["Ravi", 87],
    ["Mina", 95]
]

Path("day98_output.csv").parent.mkdir(parents=True, exist_ok=True)

with open("day98_output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("CSV created:", Path("day98_output.csv").resolve())