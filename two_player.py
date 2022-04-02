import random
from functions import *

# Accept users name's as input
player1 = input("\nEnter first player's name:\n")
player2 = input("Enter second player's name:\n")

# Print welcome message using user's name
print(f"\nWelcome to the higher/lower game, {player1} and {player2}!")

# Accept num_range as input
num_range = validate_num(input("Enter the number range:\n"), "range")
print(f"\nGuess a number between 1 and {num_range}")

# Create random number between 0 and num_range
secret_num = random.randint(1, num_range)

# Track tries and winner
tries = 0
winner = ''

# Initiate game
while winner == '':
    tries += 1
    if winner == '':
        player1_turn = guess_num(player1, num_range, secret_num)
        if player1_turn == 1:
            winner = player1
    if winner == '':
        player2_turn = guess_num(player2, num_range, secret_num)
        if player2_turn == 1:
            winner = player2

# Announce victory once while loop is exited
if tries == 1:
    print(f"\n{winner} got it in 1 try!\n"
          f"The number was {secret_num}.")
else:
    print(f"\n{winner} got it in {tries} tries!\n"
          f"The number was {secret_num}.")
