# Day 135 - task scheduler
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    priority: int

tasks = [
    Task("Email team", 2),
    Task("Fix bug", 1),
    Task("Update docs", 3),
]

for task in sorted(tasks, key=lambda t: t.priority):
    print(task.priority, task.name)