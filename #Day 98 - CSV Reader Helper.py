#Day 98 - CSV Reader Helper
from pathlib import Path
import csv

file_path = Path("day98_output.csv")

if file_path.exists():
    with file_path.open("r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"{row['name']} scored {row['score']}")
else:
    print("CSV file not found")