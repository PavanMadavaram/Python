#Day 39 - Test
class TestProp:
    def __init__(self):
        self._value = 10

    @property
    def value(self):
        return self._value

t = TestProp()
print("Property test:", t.value)
print("Day 39 test ok")
