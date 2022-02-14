from sys import argv, exit
import csv


def main():

    if len(argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    profiles = []
    with open(argv[1], "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            profiles.append(row)
    X = profiles[0]
    STRs = []
    for i in range(1, len(X), 1):
        STRs.append(X[i])

    with open(argv[2], "r") as sequence:
        reader_1 = csv.reader(sequence)
        for row in reader_1:
            dnalist = row
    dna = dnalist[0]

    STR = []
    for i in range(len(STRs)):
        seq_str_count = longest_match(dna, STRs[i])
        STR.append(seq_str_count)

    counter = 0
    for i in range(1, len(profiles), 1):
        s = profiles[i]
        test = []
        for i in range(1, len(s), 1):
            test.append(int(s[i]))
        if test == STR:
            print(s[0])
            counter += 1
        test.clear()

    if counter == 0:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
