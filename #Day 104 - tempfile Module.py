#Day 104 - tempfile Module 
import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as tmpdir:
    temp_path = Path(tmpdir) / "note.txt"
    temp_path.write_text("Hello from temporary file")
    print("Temp file exists:", temp_path.exists())
    print("Temp content:", temp_path.read_text())

print("Temp directory cleaned up automatically")