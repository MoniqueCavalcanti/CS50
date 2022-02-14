from cs50 import get_float


def main():
    n = get_float("Change owed: ")
    if n < 0:
        while n < 0:
            n = get_float("Change owed: ")

    cents = round(n * 100)
    counter25 = 0
    counter10 = 0
    counter5 = 0
    counter1 = 0
    while (cents >= 25):
        cents -= 25
        counter25 += 1
    while (cents >= 10):
        cents -= 10
        counter10 += 1
    while (cents >= 5):
        cents -= 5
        counter5 += 1
    while (cents >= 1):
        cents -= 1
        counter1 += 1

    counter = counter25 + counter10 + counter5 + counter1
    print(counter)


main()