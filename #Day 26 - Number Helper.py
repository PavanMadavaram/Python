#Day 26 - Number Helper
def number_word(num):
    words = {1:"one", 2:"two", 3:"three"}
    return words.get(num, "unknown")

print("1 =", number_word(1))
