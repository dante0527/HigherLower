import random

# Accept user's name as input
username = input("\nEnter your name:\n")

# Print welcome message using user's name
print(f"\nWelcome to the higher/lower game, {username}!")

# Accept upper and lower bounds as inputs
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Create random number between upper and lower bounds
secret_num = random.randint(lower, upper)

# Prompt user to guess number within bounds
print(f"\nGreat, now guess a number between {lower} and {upper}")

# Accept first guess
guess = int(input())
tries = 0

# Initiate while loop
while guess != secret_num:
    if lower > guess or guess > upper:
        print("Guess outside of range.\n"
              f"Guess a number between {lower} and {upper}.")
        guess = int(input())
    elif guess < secret_num:
        print("Nope, too low.")
        guess = int(input())
        tries += 1
    elif guess > secret_num:
        print("Nope, too high.")
        guess = int(input())
        tries += 1
        
# Announce victory once while loop is exited
tries += 1
if tries == 1:
    print(f"You got it in 1 try!\nThe number was {secret_num}.")
else:
    print(f"You got it in {tries} tries!\nThe number was {secret_num}.")
