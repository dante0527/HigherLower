import os

def main_menu():
    print("Welcome to Higher / Lower! Please choose an option:\n")
    version = 0
    while version not in (1, 2):
        version = int(validate_num(input("One Player (enter 1)\nTwo Player (enter 2)\n"), 'version'))
        if version == 1:
            os.system("python3 one_player.py")
        elif version == 2:
            running = True
            os.system("python3 two_player.py")
        else:
            print("Invalid version.\n")


def validate_num(num, case, *args):
    num_validated = False
    word = ''
    for x in args:
        word = x
    while not num_validated:
        try:
            assert(int(num) > 0)
            num_validated = True
            return int(num)
        except ValueError:
            print(f"\n{case.title()} must be a number")
            num = input(f"Enter {word}{case}:\n")
            pass
        except AssertionError:
            print(f"\n{case.title()} must be > 0")
            num = input(f"Enter {word}{case}:\n")
            pass


# Guess function
def guess_num(user, range, secret_num):
    guess = validate_num(input(f"{user}'s turn\n"), "guess")
    while guess > range:
        print(f"\nGuess must be between 1 and {range}.\n")
    if guess < secret_num:
        print("Nope, too low.\n")
    elif guess > secret_num:
        print("Nope, too high.\n")
    else:
        return 1

