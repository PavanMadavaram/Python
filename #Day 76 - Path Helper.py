#Day 76 - Path Helper
from pathlib import Path

# Create directory & file
test_dir = Path("test_dir")
test_dir.mkdir(exist_ok=True)

(Path(test_dir) / "hello.txt").write_text("Hello Pathlib!")
print("Created test_dir/hello.txt")

# Read file
print("Content:", (test_dir / "hello.txt").read_text())