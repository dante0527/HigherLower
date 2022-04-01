import random


# Guess function
def guess_num(user):
    global winner
    user_guess = int(input(f"\n{user}'s turn.\n"
                           f"Guess a number between {lower} and {upper}:\n"))
    if lower > user_guess or user_guess > upper:
        print("Guess outside of range.\n"
              f"Guess must be between {lower} and {upper}.")
    elif user_guess < secret_num:
        print("Nope, too low.")
    elif user_guess > secret_num:
        print("Nope, too high.")
    else:
        print(f"{user} guessed correctly!")
        winner = user


# Accept users name's as input
player1 = input("Enter first player's name:\n")
player2 = input("Enter second player's name:\n")

# Print welcome message using user's name
print(f"\nWelcome to the higher/lower game, {player1} and {player2}!")

# Accept upper and lower bounds as inputs
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Create random number between upper and lower bounds
secret_num = random.randint(lower, upper)

# Track tries and winner
tries = 0
winner = ''

# Initiate while loop
while winner == '':
    tries += 1
    if winner == '':
        guess_num(player1)
    if winner == '':
        guess_num(player2)

# Announce victory once while loop is exited
if tries == 1:
    print(f"{winner} got it in 1 try!\n"
          f"The number was {secret_num}.")
else:
    print(f"{winner} got it in {tries} tries!\n"
          f"The number was {secret_num}.")
