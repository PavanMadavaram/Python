#Day 53 - Helper
from collections import deque

recent = deque(maxlen=3)
recent.append("apple")
recent.append("banana")
recent.append("cherry")
print("Recent 3:", list(recent))