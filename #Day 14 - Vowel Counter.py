#Day 14 - Vowel Counter
def count_vowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    print(word, "has", count, "vowels")

count_vowels("Hyderabad")
