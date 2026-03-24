#Day 49 - Helper
def find_position(items, target):
    for i, item in enumerate(items):
        if item == target:
            return i
    return -1

print("Position:", find_position(["a", "b", "c"], "b"))
