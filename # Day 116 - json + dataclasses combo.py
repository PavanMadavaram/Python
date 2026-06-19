# Day 116 - json + dataclasses combo
from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass
class Task:
    title: str
    done: bool
    priority: int

tasks = [
    Task("Practice Python", True, 1),
    Task("Build project", False, 2),
    Task("Apply for jobs", False, 1),
]

Path("day116_tasks.json").write_text(json.dumps([asdict(t) for t in tasks], indent=4))
print("Saved tasks to JSON")