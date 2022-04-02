import random


# Guess function
def guess_num(user):
    global winner
    user_guess = int(input(f"\n{user}'s turn.\n"))
    if 0 > user_guess or user_guess > num_range:
        print("Guess outside of range.\n"
              f"Guess must be between 0 and {num_range}.")
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

# Accept num_range as input
num_range = int(input("Enter the num_range bound: "))

# Create random number between 0 and num_range
secret_num = random.randint(0, num_range)

# Track tries and winner
tries = 0
winner = ''

# Initiate while loop
while winner == '':
    if tries == 0:
        print(f"Guess a number between 0 and {num_range}:\n")
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
