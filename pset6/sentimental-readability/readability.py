from cs50 import get_string


def main():
    Text = get_string("Text: ")
    SystemASCII = []
    for i in range(len(Text)):
        m = ord(Text[i])
        SystemASCII.append(m)
    words = 1
    for i in range(len(SystemASCII)):
        if SystemASCII[i] == 32:
            words += 1
    phrases = 0
    for i in range(len(SystemASCII)):
        if SystemASCII[i] == 33 or SystemASCII[i] == 63 or SystemASCII[i] == 46:
            phrases += 1
    letters = 0
    for i in range(len(SystemASCII)):
        if SystemASCII[i] >= 65 and SystemASCII[i] <= 122:
            letters += 1
    L = (letters / words) * 100
    S = (phrases / words) * 100
    X = round((0.0588 * L) - (0.296 * S) - 15.8)
    if X < 1:
        print("Before Grade 1")
    elif X >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {X}")


main()