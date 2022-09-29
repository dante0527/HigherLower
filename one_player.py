from main import validate_num, clear
import random

def one_player():

    # Print welcome message
    print("Welcome to the higher/lower game!")

    # Get num_range and generate secret_num
    num_range = validate_num(input("Enter the number range:\n"), "range")
    secret_num = random.randint(1, num_range)
    clear()

    # Accept first guess
    guess = validate_num(input(f"Great, now guess a number between 1 and {num_range}:\n"), "guess")
    tries = 0

    # Initiate while loop
    while guess != secret_num:
        
        # Guess outside of range
        if guess > num_range:
            clear()
            guess = validate_num(input("Guess outside of range.\n"
                f"Guess a number between 1 and {num_range}:\n"), "guess")

        # Guess too low
        elif guess < secret_num:
            tries += 1
            clear()
            guess = validate_num(input("Nope, too low.\nEnter your guess:\n"), "guess")

        # Guess too high
        elif guess > secret_num:
            tries += 1
            clear()
            guess = validate_num(input("Nope, too high.\nEnter your guess:\n"), "guess")

    # Announce victory
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
    