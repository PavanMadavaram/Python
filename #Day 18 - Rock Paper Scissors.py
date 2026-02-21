#Day 18 - Rock Paper Scissors
import random

player = "rock"
computer = random.choice(["rock", "paper", "scissors"])

print("You chose:", player)
print("Computer chose:", computer)

if player == computer:
    print("Tie!")
elif player == "rock" and computer == "scissors":
    print("You win!")
elif player == "paper" and computer == "rock":
    print("You win!")
elif player == "scissors" and computer == "paper":
    print("You win!")
else:
    print("Computer wins!")
