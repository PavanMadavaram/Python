#Day 27 - File Helper
def write_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return "File written"

print(write_file("data.txt", "Day 27 data"))
