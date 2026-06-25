# Day 122 - Test
from collections import defaultdict

g = defaultdict(list)
g["txt"].append("a.txt")
print("Day 122 test:", g["txt"] == ["a.txt"])
print("Day 122 test ok")