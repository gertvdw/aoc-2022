const fs = require("fs");

const pairs = fs
  .readFileSync("inputs/day13.txt", "utf-8")
  .replace(/\r/g, "")
  .split(/\n\n/g);
const j = (s) => JSON.stringify(s);
const compareLists = (listA, listB) => {
  const max = Math.max(listA.length, listB.length);
  for (let i = 0; i < max; i++) {
    const left = listA[i];
    const right = listB[i];
    // console.log(`... ${j(left)} vs ${j(right)}`);

    if (left === undefined && right === undefined) return null;
    if (left === undefined) return true;
    if (right === undefined) return false;

    if (typeof left === "number" && typeof right === "number") {
      if (left === right) continue;
      return left < right;
    }
    const result = compareLists(
      Array.isArray(listA[i]) ? listA[i] : [listA[i]],
      Array.isArray(listB[i]) ? listB[i] : [listB[i]]
    );
    if (result !== null) return result;
  }
  return null;
};

const convert = (str) => {
  return eval(str);
};

const workingPairs = [];
for (const pair of pairs) {
  const parts = pair.split(/\n/).map((p) => convert(p));
  workingPairs.push(parts);
}

console.log(compareLists(workingPairs[6][0], workingPairs[6][1]));
const orderedPairs = workingPairs.map(([left, right]) =>
  compareLists(left, right)
);
const sumOfOrderedPairs = orderedPairs.reduce(
  (sum, result, idx) => sum + (result === true ? idx + 1 : 0),
  0
);

console.log(`p1: ${sumOfOrderedPairs}`);
