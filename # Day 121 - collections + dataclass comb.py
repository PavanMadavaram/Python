# Day 121 - collections + dataclass combo
from dataclasses import dataclass
from collections import Counter

@dataclass
class Vote:
    name: str
    choice: str

votes = [
    Vote("Asha", "Python"),
    Vote("Ravi", "Python"),
    Vote("Mina", "SQL"),
    Vote("Kiran", "Python"),
    Vote("Nikhil", "SQL"),
]

counts = Counter(v.choice for v in votes)

print("Vote counts:", counts)
print("Winner:", counts.most_common(1)[0][0])