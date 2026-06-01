# Day 100  -  final wrap-up
from pathlib import Path

summary = [
    "Completed 100 days of Python.",
    "Covered built-in modules, file handling, concurrency, databases, and more.",
    "Built small scripts every day.",
    "Kept improving consistency and confidence."
]

Path("day100_summary.txt").write_text("\n".join(summary))
print("Day 100 complete!")
for line in summary:
    print("-", line)
    
