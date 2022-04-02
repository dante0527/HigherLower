import random

# Accept user's name as input
username = input("\nEnter your name:\n")

# Print welcome message using user's name
print(f"\nWelcome to the higher/0 game, {username}!")

# Accept number range as input
num_range = int(input("Enter the number range: "))

# Create random number between 0 and num_range
secret_num = random.randint(0, num_range)

# Prompt user to guess number within bounds
print(f"\nGreat, now guess a number between 0 and {num_range}")

# Accept first guess
guess = int(input())
tries = 0

# Initiate while loop
while guess != secret_num:
    if 0 > guess or guess > num_range:
        print("Guess outside of range.\n"
              f"Guess a number between 0 and {num_range}.")
        guess = int(input())
    elif guess < secret_num:
        tries += 1
        print("Nope, too low.")
        guess = int(input())
    elif guess > secret_num:
        tries += 1
        print("Nope, too high.")
        guess = int(input())
        
# Announce victory once while loop is exited
tries += 1
if tries == 1:
    print(f"\nYou got it in 1 try!\nThe number was {secret_num}.")
else:
    print(f"\nYou got it in {tries} tries!\nThe number was {secret_num}.")
