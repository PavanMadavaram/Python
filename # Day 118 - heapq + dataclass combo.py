# Day 118 - heapq + dataclass combo
from dataclasses import dataclass, field
import heapq

@dataclass(order=True)
class Job:
    priority: int
    title: str = field(compare=False)

jobs = [
    Job(3, "Clean inbox"),
    Job(1, "Fix bug"),
    Job(2, "Write report"),
]

heapq.heapify(jobs)
print("First job:", heapq.heappop(jobs))
print("Remaining:", jobs)