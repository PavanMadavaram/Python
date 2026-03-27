#Day 51 - collections.namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p.x}, {p.y}")
print("As tuple:", p)
