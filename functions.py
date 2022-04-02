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
            print(f"\n{case.title()} must be positive")
            num = input(f"Enter {word}{case}:\n")
            pass
