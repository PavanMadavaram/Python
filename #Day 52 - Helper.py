#Day 52 - Helper
from collections import defaultdict

grades = defaultdict(list)
grades['Sai'].append(85)
grades['Ram'].append(92)
print("Student grades:", dict(grades))