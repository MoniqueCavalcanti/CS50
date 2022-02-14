from cs50 import get_int


def main():
    n = get_int("Height: ")
    if n > 8 or n < 1:
        while n > 8 or n < 1:
            n = get_int("Height: ")
    for i in range(1, n + 1, 1):
        for j in range(0, n - i, 1):
            print(" ", end="")
        for k in range(0, i, 1):
            print("#", end="")
        print("  ", end="")
        for l in range(0, i, 1):
            print("#", end="")
        print()


main()