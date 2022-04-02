import random
from functions import *

# Print welcome message
print(f"\nWelcome to the higher/lower game!")

# Accept number range as input
num_range = validate_num(input("Enter the number range:\n"), "range")

# Create random number between 0 and num_range
secret_num = random.randint(1, num_range)

# Prompt player to guess number within bounds
print(f"\nGreat, now guess a number between 1 and {num_range}")

# Accept first guess
guess = validate_num(input(), "guess", "your ")
tries = 0

# Initiate while loop
while guess != secret_num:
    if guess > num_range:
        print("Guess outside of range.\n"
              f"Guess a number between 0 and {num_range}.")
        guess = validate_num(input(), "guess", "your")
    elif guess < secret_num:
        tries += 1
        print("Nope, too low.")
        guess = validate_num(input(), "guess", "your")
    elif guess > secret_num:
        tries += 1
        print("Nope, too high.")
        guess = validate_num(input(), "guess", "your")

# Announce victory once while loop is exited
tries += 1
if tries == 1:
    print(f"\nYou got it in 1 try!\nThe number was {secret_num}.")
else:
    print(f"\nYou got it in {tries} tries!\nThe number was {secret_num}.")
