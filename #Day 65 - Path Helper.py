#Day 65 - Path Helper
from pathlib import Path

file_path = Path("test.txt")
if file_path.exists():
    print("File exists")
else:
    print("File not found")