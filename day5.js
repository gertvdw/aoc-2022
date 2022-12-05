const fs = require("fs");

const part = Number(process.argv[2]) || 1;

const inputData = fs.readFileSync("inputs/day5.txt").toString().split(/\n/).map(s => s.trimEnd());
const columns = 9;
const stacks = [];
for (let c = 0; c < columns; c++) {
  stacks[c] = [];
}

for (let i = 0; i < 8; i++) {
  const line = inputData.shift();
  for (let j = 0; j < columns; j++) {
    const part = line.substring(j*4, Math.min(j*4+4, line.length)).trimEnd();
    if (part !== "") {
      stacks[j].unshift(part);
    }
  }
}

/**
 * Dump the stacks in reverse order,
 * so we get the same graphic as used in the data table.
 */
function dumpStacks() {
  const dump = [...stacks];
  const strs = [];
  let i = 0;
  let painted = true;
  while (painted) {
    painted = false;
    let line = "";
    for (const s of dump) {
      if (i < s.length) {
        line += `${s[i]} `;
        painted = true;
      } else {
        line += "    ";
      }
    }
    strs.unshift(`${line}`);
    if (!painted) {
      break;
    }
    i++;
  }
  console.log(strs.join("\n"));
}

// part 1
if (part === 1) {
  for (let i = 2; i < inputData.length; i++) {
    const m = inputData[i].match(/move (\d+) from (\d) to (\d)/);
    const [all, amount, source, target] = m;
    for (let c = 0; c < amount; c++) {
      stacks[target - 1].push(stacks[source - 1].pop());
    }
  }
} else {
  // part 2
  for (let i = 2; i < inputData.length; i++) {
    const m = inputData[i].match(/move (\d+) from (\d) to (\d)/);
    const [all, amount, source, target] = m;
    stacks[target - 1].push(...stacks[source - 1].splice(amount * -1));  
  }
}

dumpStacks();