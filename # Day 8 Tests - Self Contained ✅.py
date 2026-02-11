# Day 8 Tests - Self Contained ✅
person = {"name": "Pavan", "age": 22, "city": "Hyderabad"}
print("Name:", person["name"])
print("Age:", person["age"])
print("Keys:", list(person.keys()))

assert person["age"] == 22, "Age test failed!"
assert "city" in person, "City key missing!"
print("✅ Day 8: All dictionary tests PASSED!")
