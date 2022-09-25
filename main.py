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


if __name__ == "__main__":
    version = 0
    clear()
    main_menu()
