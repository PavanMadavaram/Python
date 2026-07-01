# Day 128 - Test
from dataclasses import dataclass

@dataclass
class Note:
    title: str
    body: str

n = Note("T", "B")
print("Day 128 test:", n.title == "T" and n.body == "B")
print("Day 128 test ok")