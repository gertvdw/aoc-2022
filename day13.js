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

const orderedPairs = workingPairs.map(([left, right]) =>
  compareLists(left, right)
);
const sumOfOrderedPairs = orderedPairs.reduce(
  (sum, result, idx) => sum + (result === true ? idx + 1 : 0),
  0
);
const sortPackets = (a, b) => {
  const r = compareLists(a, b);
  if (r === null) return 0;
  return r ? -1 : 1;
};
console.log(`p1: ${sumOfOrderedPairs}`);

const sep = [[[2]], [[6]]];
const sepStr = sep.map((s) => JSON.stringify(s));
const allPackets = [...workingPairs.flatMap((pair) => pair), ...sep];

const sortedPackets = allPackets.sort(sortPackets);
const decoderKey = sortedPackets.reduce(
  (acc, v, i) => acc * (sepStr.includes(JSON.stringify(v)) ? i + 1 : 1),
  1
);
console.log(`p2: ${decoderKey}`);
