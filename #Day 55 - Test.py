#Day 55 - Test
class TestError(Exception):
    pass

try:
    raise TestError("Test")
except TestError:
    print("Custom exception caught")
print("Day 55 test ok")