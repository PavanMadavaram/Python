#Day 54 - Test
try:
    x = 1 / 0
except Exception as e:
    print("Caught:", type(e).__name__)
print("Day 54 test ok")