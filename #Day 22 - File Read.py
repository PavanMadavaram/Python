#Day 22 - File Read
with open("notes.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)
