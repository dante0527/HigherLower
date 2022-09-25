import os

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main_menu():
    global version
    from one_player import one_player
    from two_player import two_player

    print("Welcome to Higher / Lower! Please choose an option:\n")
    
    while version not in (1, 2):
        version = input("One Player (enter 1)\nTwo Player (enter 2)\n")
        clear()
        if version == '1':
            one_player()
            break
        elif version == '2':
            two_player()
            break
        else:
            print("Invalid version.\n")


def validate_num(num, type, *args):
    player = args

    while True:
        try:
            assert(int(num) > 0)
            return int(num)
        
        # NaN
        except ValueError:
            clear()
            print(f"{type.title()} must be a number.")

            if player:
                print(f"{player[0]}'s turn")

            num = input(f"Enter {type}:\n")
            pass
        
        # Negative number
        except AssertionError:
            clear()
            print(f"{type.title()} must be > 0")

            if player:
                print(f"{player[0]}'s turn")

            num = input(f"Enter {type}:\n")
            pass


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


if __name__ == "__main__":
    version = 0
    clear()
    main_menu()
