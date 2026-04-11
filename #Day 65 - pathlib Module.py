#Day 65 - pathlib Module 
from pathlib import Path

current_dir = Path(".")
python_files = list(current_dir.glob("*.py"))
print("Python files:", len(python_files))