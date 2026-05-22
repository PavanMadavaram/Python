#Day 91 - zipfile Module 
import zipfile
from pathlib import Path

# Create sample files
Path("file1.txt").write_text("Hello from file 1")
Path("file2.txt").write_text("Hello from file 2")

# Create ZIP archive
with zipfile.ZipFile("day91_archive.zip", "w") as zipf:
    zipf.write("file1.txt")
    zipf.write("file2.txt")

print("ZIP created:", "day91_archive.zip")