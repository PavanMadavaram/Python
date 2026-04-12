#Day 66 - random Module Advanced
import random

# Shuffle list
cards = ["Ace", "King", "Queen"]
random.shuffle(cards)
print("Shuffled cards:", cards)

# Random choice
choice = random.choice(["Rock", "Paper", "Scissors"])
print("Random choice:", choice)