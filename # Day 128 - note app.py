# Day 128 - note app
from dataclasses import dataclass

@dataclass
class Note:
    title: str
    body: str

notes = [
    Note("Buy milk", "2 liters"),
    Note("Study", "Review Python files"),
    Note("Workout", "30 minutes"),
]

for note in notes:
    print(f"{note.title}: {note.body}")