import os
import title_art
from one_player import *
from two_player import *

def main_menu():
    print("Welcome to Higher / Lower! Please choose an option:\n")
    version = 0
    while version not in (1, 2):
        version = int(validate_num(input("One Player (enter 1)\nTwo Player (enter 2)\n"), 'version'))
        clear()
        if version == 1:
            one_player()
        elif version == 2:
            two_player()
        else:
            print("Invalid version.\n")


def validate_num(num, type):
    num_validated = False
    while True:
        try:
            assert(int(num) > 0)
            return int(num)
            break
        except ValueError:
            clear()
            print(f"\n{type.title()} must be a number.")
            num = input(f"Enter {type}:\n")
            pass
        except AssertionError:
            clear()
            print(f"\n{type.title()} must be > 0.\n")
            num = input(f"Enter {type}:\n")
            pass


# Guess function
def guess_num(player, range, secret_num):
    clear()
    guess = validate_num(input(f"{player}'s turn\n"), "guess")
    while 0 > guess > range:
        print(f"\nGuess must be between 1 and {range}.\n")
    if guess < secret_num:
        clear()
        print("Nope, too low.\n")
    elif guess > secret_num:
        clear()
        print("Nope, too high.\n")


# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":

    # Title art
    print(title_art.higher_lower)

    # Run Program
    main_menu()
