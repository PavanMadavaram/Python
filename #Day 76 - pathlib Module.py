#Day 76 - pathlib Module 
from pathlib import Path

# Current directory
p = Path('.')
print("Current dir files:")
for file in p.iterdir():
    if file.is_file():
        print(f"  {file.name}")

# Home directory
home = Path.home()
print("Home:", home)