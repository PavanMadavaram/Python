#Day 43 - Helper
words = ["apple", "bat", "cat"]

# Lengths
lengths = list(map(lambda w: len(w), words))
print("Lengths:", lengths)

# Words > 3 letters
long = list(filter(lambda w: len(w) > 3, words))
print("Long words:", long)
