#Day 42 - Test
def simple_gen():
    yield 1
    yield 2

nums = list(simple_gen())
print("Generator test:", nums)
print("Day 42 test ok")
