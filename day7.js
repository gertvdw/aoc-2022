const fs = require("fs");

const createNode = (name, parent) => ({
  parent,
  name,
  size: 0,
  children: [],
});

const tree = [createNode("/")];
const directories = [];

const data = fs.readFileSync("inputs/day7.txt", "utf-8").toString();
let currentNode = tree[0];

for (const line of data.split("\n")) {
  const dirChange = line.match(/\$ cd (.*)/);
  const foundDir = line.match(/dir (.*)/);
  const foundFile = line.match(/(\d+) ([a-z.]+)/);

  if (line.startsWith("$ cd /")) {
    currentNode = tree[0];
  } else if (dirChange) {
    switch (dirChange[1]) {
      case "..":
        currentNode = currentNode.parent;
        break;
      default:
        currentNode = currentNode.children.find(
          (node) => node.name === dirChange[1]
        );
    }
  }

  if (foundDir) {
    const newNode = createNode(foundDir[1], currentNode);
    currentNode.children.push(newNode);
  } else if (foundFile) {
    const newNode = createNode(foundFile[2], currentNode);
    newNode.size = parseInt(foundFile[1]);
    currentNode.children.push(newNode);
  }
}

const printTree = (node) => {
  const size = sizeTree(node);
  const isLeaf = node.children.length === 0;
  if (!isLeaf) {
    directories.push({
      name: node.name,
      size,
    });
  }
  console.group(`${size} ${node.name}`);
  for (const child of node.children) {
    printTree(child);
  }
  console.groupEnd();
};

const sizeTree = (node) => {
  if (node.size > 0) {
    return node.size;
  }
  if (node.children.length > 0) {
    const size = node.children.reduce((acc, child) => acc + sizeTree(child), 0);
    return size;
  }
};

printTree(tree[0]);

console.log("Day 7, part 1: Directories with at most 100.000 size");
const part1 = directories
  .filter((dir) => dir.size <= 100000)
  .map((dir) => dir.size)
  .reduce((acc, dir) => acc + dir, 0);
console.log(`Total size of dirs < 100.000: ${part1}`);

console.log("Day 7, part 2: free up 30000000");
const totalSpaceUsed = sizeTree(tree[0]);
const diskSize = 70000000;
const spaceNeeded = 30000000;
const needToFree = spaceNeeded - (diskSize - totalSpaceUsed);
console.group("space");
console.log(`Disk: ${diskSize}`);
console.log(`Used: ${totalSpaceUsed}`);
console.log(`Free: ${diskSize - totalSpaceUsed}`);
console.log(`Reqd: ${spaceNeeded}`);
console.log(`Need: ${needToFree}`);
console.groupEnd();
const part2 = directories
  .filter((dir) => dir.size >= needToFree)
  .sort((a, b) => a.size - b.size);
console.log("Smallest directory with correct size:", part2[0]);
