#Day 44 - Test
class TestContext:
    def __enter__(self):
        print("Enter")
        return "test"
    
    def __exit__(self, *args):
        print("Exit")

with TestContext() as t:
    print("Inside:", t)
print("Day 44 test ok")
