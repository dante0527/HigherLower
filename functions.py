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

