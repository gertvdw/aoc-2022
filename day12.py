with open("inputs/day12.txt") as f:
    data = f.readlines()


class Node():
    def __init__(self, score, name, y, x):
        self.adjacent = []
        self.dist = 1e7
        self.score = score
        self.seen = False
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return "<%s,%s>" % (self.name, self.dist)


def to_vertice(row):
    return [assign_value(l) for l in row]


def assign_value(letter):
    if letter == "S":
        return 96
    if letter == "E":
        return 123
    return ord(letter)


def find_adjacent_nodes(node):
    for n in nodes:
        if n.x == node.x - 1 and n.y == node.y:
            yield n
        if n.x == node.x + 1 and n.y == node.y:
            yield n
        if n.x == node.x and n.y == node.y - 1:
            yield n
        if n.x == node.x and n.y == node.y + 1:
            yield n


def pop_min_dist(queue):
    bestIndex = 0
    max = 1e7
    for index, value in enumerate(queue):
        if value.dist < max:
            max = value.dist
            bestIndex = index
    return queue.pop(bestIndex)


def dijkstra(nodes, source):
    queue = []
    for n in nodes:
        queue.append(n)
    source.dist = 0

    while len(queue) > 0:
        current = pop_min_dist(queue)
        current.seen = True
        for neigh in current.adjacent:
            if not neigh.seen:
                newDist = current.dist + 1
                if newDist < neigh.dist:
                    neigh.dist = newDist
                    neigh.prev = current


vertices = [to_vertice(r.rstrip()) for r in data]
vertice_count = len(vertices)
nodes = []
for a in range(0, len(vertices)):
    for b in range(0, len(vertices[a])):
        node = Node(vertices[a][b], data[a][b], b, a)
        nodes.append(node)

source = None

for node in nodes:
    for a in find_adjacent_nodes(node):
        if node.score <= (a.score + 1):
            node.adjacent.append(a)
    if node.score == 123:
        source = node

dijkstra(nodes, source)
part2_dist = 1e7
for n in nodes:
    if n.name == "S":
        print("Day 12, part 1: %d steps" % n.dist)
    if n.name == "a" and n.dist < part2_dist:
        part2_dist = n.dist

print("Day 12, part 2: %d steps" % part2_dist)
