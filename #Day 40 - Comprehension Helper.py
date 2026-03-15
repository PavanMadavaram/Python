#Day 40 - Comprehension Helper
words = ["apple", "banana", "cherry"]

# Lengths
lengths = [len(word) for word in words]
print("Lengths:", lengths)

# Long words
long_words = [w for w in words if len(w) > 5]
print("Long words:", long_words)
