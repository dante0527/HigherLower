from main import validate_num, clear
import random

def one_player():

    # Print welcome message
    print(f"Welcome to the higher/lower game!")

    # Accept number range as input
    num_range = validate_num(input("Enter the number range:\n"), "range")
    clear()

    # Create random number between 0 and num_range
    secret_num = random.randint(1, num_range)

    # Prompt player to guess number within bounds
    print(f"Great, now guess a number between 1 and {num_range}:")

    # Accept first guess
    guess = validate_num(input(), "guess")
    tries = 0

    # Initiate while loop
    while guess != secret_num:
        
        # Guess outside of range
        if guess > num_range:
            clear()
            print("Guess outside of range.\n"
                f"Guess a number between 1 and {num_range}:")
            guess = validate_num(input(), "guess")

        # Guess too low
        elif guess < secret_num:
            tries += 1
            clear()
            print("Nope, too low.\nEnter your guess:")
            guess = validate_num(input(), "guess")

        # Guess too high
        elif guess > secret_num:
            tries += 1
            clear()
            print("Nope, too high.\nEnter your guess:")
            guess = validate_num(input(), "guess")

    # Announce victory once while loop is exited
    tries += 1
    if tries == 1:
        clear()
        print(f"You got it in 1 try!\nThe number was {secret_num}.")
    else:
        clear()
        print(f"You got it in {tries} tries!\nThe number was {secret_num}.")


if __name__ == "__main__":
    clear()
    one_player()
    