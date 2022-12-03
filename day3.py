with open("inputs/day3.txt") as file:
    data = file.read()

def letter_value(letter: str) -> int:
    v = ord(letter)
    return v - 96 if v > 90 else v - 38

def common_letter(item1: str, item2: str, item3: str) -> str:
    for c in item1:
        if c in item2 and c in item3:
            return c
    return None

def process_contents():
    priorities = []
    badges = []
    lines = data.split("\n")
    for line in lines:
        l = int(len(line) / 2)
        priorities.append(letter_value(common_letter(line[:l], line[l:], line[l:])))

    for i in range(0, len(lines) - 1, 3):
        badges.append(letter_value(common_letter(lines[i], lines[i+1], lines[i+2])))
    print("Sum of priorities: %d" % sum(priorities))
    print("Sum of badges: %d" % sum(badges))



if __name__ == "__main__":
    process_contents()