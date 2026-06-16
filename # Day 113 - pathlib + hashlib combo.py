# Day 113 - pathlib + hashlib combo
from pathlib import Path
import hashlib

text = "Day 113 makes progress"
path = Path("day113_note.txt")
path.write_text(text)

digest = hashlib.sha256(path.read_bytes()).hexdigest()
print("File written:", path.exists())
print("SHA256:", digest)