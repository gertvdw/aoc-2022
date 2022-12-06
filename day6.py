with open("inputs/day6.txt") as f:
    data = f.read()


def find_unique_sequence(sequence_length):
    part = 1 if sequence_length == 4 else 2
    for i in range(0, len(data) - sequence_length):
        chunk = data[i:i+sequence_length]
        if len(chunk) == len(set(chunk)):
            print("Day 6, part %d: Marker found after %d" %
                  (part, i + sequence_length))
            break


if __name__ == "__main__":
    find_unique_sequence(4)
    find_unique_sequence(14)
