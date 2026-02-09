# Day 6 Tests - Self Contained
fruits = ["apple", "banana", "orange"]
print("First fruit:", fruits[0])
print("Length:", len(fruits))
fruits.append("mango")
print("Updated list:", fruits)

assert len(fruits) == 4, "Length test failed!"
print("✅ Day 6: All tests PASSED!")
