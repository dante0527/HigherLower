from main import validate_num, clear
import random

# Two player guess function
def guess_num(player, range, secret_num):
    guess = validate_num(input(f"{player}'s turn\nEnter guess:\n"), "guess", player)

    # Guess outside of range
    while guess > range:
        clear()
        print(f"Guess must be between 1 and {range}\n{player}'s turn\nEnter guess:")
        guess = validate_num(input(), "guess", player)

    # Guess too low
    if guess < secret_num:
        clear()
        print("Nope, too low.")
    
    # Guess too high
    elif guess > secret_num:
        clear()
        print("Nope, too high.")

    # Correct guess
    else:
        return 1


def two_player():
    # Accept users name's as input
    player1 = input("Enter first player's name:\n").title()
    clear()
    player2 = input("Enter second player's name:\n").title()
    clear()

    # Print welcome message using user's name
    print(f"Welcome to the higher/lower game, {player1} and {player2}!")

    # Accept num_range as input
    num_range = validate_num(input("Enter the number range:\n"), "range")
    clear()
    print(f"Guess a number between 1 and {num_range}")

    # Create random number between 0 and num_range
    secret_num = random.randint(1, num_range)

    # Track tries and winner
    tries = 0
    winner = ''

    # Gameplay loop
    while winner == '':
        tries += 1
        if winner == '':
            if guess_num(player1, num_range, secret_num) == 1:
                winner = player1
        if winner == '':
            if guess_num(player2, num_range, secret_num) == 1:
                winner = player2

    # Announce victory once while loop is exited
    if tries == 1:
        clear()
        print(f"{winner} got it in 1 try!\nThe number was {secret_num}.")
    else:
        clear()
        print(f"{winner} got it in {tries} tries!\nThe number was {secret_num}.")


if __name__ == "__main__":
    clear()
    two_player()
