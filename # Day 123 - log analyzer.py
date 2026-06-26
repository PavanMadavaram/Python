# Day 123 - log analyzer
from collections import Counter

logs = [
    "INFO login success",
    "ERROR db timeout",
    "INFO profile loaded",
    "WARNING disk space low",
    "ERROR cache miss",
]

levels = Counter(line.split()[0] for line in logs)

for level, count in levels.items():
    print(level, count)