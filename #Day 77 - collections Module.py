#Day 77 - collections Module 
from collections import Counter, namedtuple, deque

# Counter
text = "hello world"
count = Counter(text)
print("Counter:", dict(count))

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print("Point:", p.x, p.y)