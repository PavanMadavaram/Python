# Day 122 - Organizer Helper
from pathlib import Path

paths = [Path("a.py"), Path("b.md"), Path("c.py")]
print([p.suffix for p in paths])