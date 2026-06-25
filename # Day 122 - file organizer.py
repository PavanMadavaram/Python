# Day 122 - file organizer
from pathlib import Path
from collections import defaultdict

files = ["notes.txt", "photo.jpg", "report.pdf", "todo.txt", "diagram.png", "draft.pdf"]
groups = defaultdict(list)

for name in files:
    ext = Path(name).suffix.lower().lstrip(".") or "no_ext"
    groups[ext].append(name)

for ext, items in groups.items():
    print(ext, ":", items)