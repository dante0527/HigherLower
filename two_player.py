import random


# Guess function
def guess_num(user):
    global winner
    guess = int(input(f"{user}'s turn\n"))
    if (0 > guess) or (guess > num_range) or (guess == ''):
        print(f"Guess must be between 0 and {num_range}.\n")
    elif guess < secret_num:
        print("Nope, too low.\n")
    elif guess > secret_num:
        print("Nope, too high.\n")
    else:
        winner = user


# Accept users name's as input
player1 = input("\nEnter first player's name:\n")
player2 = input("Enter second player's name:\n")

# Print welcome message using user's name
print(f"\nWelcome to the higher/lower game, {player1} and {player2}!")

# Accept num_range as input
num_range = -1
while num_range == -1:
    num_range0 = input("Enter the number range: ")
    while (isinstance(num_range0, int) == False) or (num_range0 < 0):
        if isinstance(num_range0, int) == False:
            num_range0 = input("Number range must be a number.\nEnter the number range: ")
            pass
        if num_range0 < 0:
            num_range0 = int(input("Number range must be positive.\nEnter the number range: "))
    num_range = num_range0
print(f"\nGuess a number between 0 and {num_range}")

# Create random number between 0 and num_range
secret_num = random.randint(0, num_range)

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
    print(f"\n{winner} got it in 1 try!\n"
          f"The number was {secret_num}.")
else:
    print(f"\n{winner} got it in {tries} tries!\n"
          f"The number was {secret_num}.")
