# Day 113 - Hash Helper
from pathlib import Path
import hashlib

p = Path("day113_note.txt")
if p.exists():
    md5 = hashlib.md5(p.read_bytes()).hexdigest()
    print("MD5:", md5)
else:
    print("File missing")