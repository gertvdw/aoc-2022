def source_contains_target(source: tuple, target: tuple) -> bool:
    return target[0] >= source[0] and target[1] <= source[1]


def source_intersects_target(source: tuple, target: tuple) -> bool:
    return target[0] <= source[1] and target[1] >= source[0]


def process_line(line: str):
    elves = line.split(",")
    source = [int(i) for i in elves[0].split("-")]
    target = [int(i) for i in elves[1].split("-")]
    part1 = source_contains_target(
        source, target) or source_contains_target(target, source)
    part2 = source_intersects_target(
        source, target) or source_intersects_target(target, source)
    return part1, part2


fully_contained = 0
overlapping = 0

with open("inputs/day4.txt") as f:
    data = f.read()
    for line in data.split("\n"):
        rv = process_line(line)
        if rv[0]:
            fully_contained += 1
        if rv[1]:
            overlapping += 1


print("Day 4, part 1: %d" % fully_contained)
print("Day 4, part 2: %d" % overlapping)
