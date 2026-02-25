#Day 22 - Test
try:
    with open("test.txt", "r") as f:
        print("Test file read ok")
except FileNotFoundError:
    print("File test - create first")
print("Day 22 test complete")
