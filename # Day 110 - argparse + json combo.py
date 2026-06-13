# Day 110 - argparse + json combo
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description="Day 110 profile saver")
parser.add_argument("--name", default="Guest")
parser.add_argument("--city", default="Hyderabad")
parser.add_argument("--age", type=int, default=0)
args = parser.parse_args([])

profile = {
    "name": args.name,
    "city": args.city,
    "age": args.age
}

Path("day110_profile.json").write_text(json.dumps(profile, indent=4))
print("Profile saved:", profile)