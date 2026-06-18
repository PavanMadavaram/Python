# Day 115 - pathlib + csv report
from pathlib import Path
import csv

rows = [
    ["topic", "count"],
    ["Python", 115],
    ["Practice", 115],
    ["Consistency", 115],
]

with open("day115_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print("CSV saved:", Path("day115_report.csv").exists())