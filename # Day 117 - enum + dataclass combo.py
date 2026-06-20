# Day 117 - enum + dataclass combo
from dataclasses import dataclass
from enum import Enum, auto

class Priority(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

@dataclass
class Ticket:
    title: str
    priority: Priority
    done: bool = False

tickets = [
    Ticket("Fix login bug", Priority.HIGH),
    Ticket("Update README", Priority.LOW, True),
    Ticket("Add analytics", Priority.MEDIUM),
]

for t in tickets:
    print(t.title, t.priority.name, t.done)