#Day 56 - Helper
from typing import List

def average(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)

grades: List[float] = [85.5, 92.0]
print("Average:", average(grades))