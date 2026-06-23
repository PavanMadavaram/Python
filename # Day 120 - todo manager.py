# Day 120 - todo manager
from dataclasses import dataclass, asdict
import json
from pathlib import Path

@dataclass
class Todo:
    title: str
    done: bool = False

todos = [
    Todo("Apply for jobs"),
    Todo("Practice Python"),
    Todo("Review GitHub"),
]

Path("day120_todos.json").write_text(json.dumps([asdict(t) for t in todos], indent=4))
print("Saved todos to day120_todos.json")