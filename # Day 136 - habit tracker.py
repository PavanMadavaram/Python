# Day 136 - habit tracker
from dataclasses import dataclass

@dataclass
class Habit:
    name: str
    streak: int

habits = [
    Habit("Read", 5),
    Habit("Exercise", 12),
    Habit("Code", 20),
]

for h in habits:
    print(f"{h.name}: {h.streak} days")