#Day 56 - Type Hints 
def add(a: int, b: int) -> int:
    return a + b

name: str = "Sai"
scores: list[int] = [85, 92, 78]

print("Sum:", add(5, 3))
print("Name:", name)