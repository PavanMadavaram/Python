
# Day 2 Tests - Self Contained (No imports needed)
def test_add():
    result = 2 + 3
    print("Test 2 + 3 =", result)
    assert result == 5, "Add test failed!"

def test_subtract():
    result = 10 - 4
    print("Test 10 - 4 =", result)
    assert result == 6, "Subtract test failed!"

def test_multiply():
    result = 5 * 6
    print("Test 5 * 6 =", result)
    assert result == 30, "Multiply test failed!"

# Run tests
test_add()
test_subtract()
test_multiply()
print("✅ All Day 2 tests PASSED!")
