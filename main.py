import os

# Clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Menu screen
def main_menu():
    global version
    from one_player import one_player
    from two_player import two_player

    print("Welcome to Higher / Lower! Please choose an option:\n")
    
    while True:
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


# Validate input
def validate_num(num, type, *args):

    # Player's name (2P only)
    player = args

    # Input must be a positive integer
    while True:

        try:
            assert(int(num) > 0)
            return int(num)
        
        # NaN
        except ValueError:
            clear()

            # Error message
            print(f"{type.title()} must be a number.")

            # Turn message (2P only)
            if player:
                print(f"{player[0]}'s turn")

            # Get new input
            num = input(f"Enter {type}:\n")
            pass
        
        # Negative number
        except AssertionError:
            clear()

            # Error message
            print(f"{type.title()} must be > 0")

            # Turn message (2P only)
            if player:
                print(f"{player[0]}'s turn")

            # Get new input
            num = input(f"Enter {type}:\n")
            pass


if __name__ == "__main__":
    version = 0
    clear()
    main_menu()
