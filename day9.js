let data = [];
let visual = false;

function loadData() {
  data = this.responseText.split("\n").map((line) => line.split(" "));
  console.log(solve(2));
}

if (typeof window === "undefined" || !window) {
  const fs = require("fs");
  data = fs
    .readFileSync("inputs/day9.txt", "utf8")
    .split("\n")
    .map((line) => line.split(" "));
} else {
  visual = true;
  const xhr = new XMLHttpRequest();
  xhr.addEventListener("load", loadData);
  xhr.open("GET", "http://localhost:8080/inputs/day9.txt");
  xhr.send();
}

// Preset the directions we can move.
const directions = {
  R: [1, 0],
  L: [-1, 0],
  U: [0, -1],
  D: [0, 1],
};

function initCanvas() {
  const canvas = document.getElementById("canvas");
  const ctx = canvas.getContext("2d");
  ctx.translate(500, 400);
  return {
    canvas,
    ctx,
    w: 5,
  };
}

function drawRope(ctx, rope) {
  // ctx.ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
  //for (const segment of rope) {
  segment = rope[0];
  ctx.ctx.fillStyle = "#ff0000";
  ctx.ctx.fillRect(
    segment[0] * ctx.w,
    segment[1] * ctx.w,
    ctx.w - 1,
    ctx.w - 1
  );
  //}
}

const solve = (ropeLength) => {
  // store visited locations in a set, for uniqueness
  const tailVisited = new Set();
  let ctx = {};
  if (visual) {
    ctx = initCanvas();
  }
  // snaaaaaake
  let rope = Array.from(
    {
      length: ropeLength,
    },
    () => [0, 0]
  );

  data.map((move) => {
    let [direction, steps] = move;
    steps = Number(steps);
    for (let i = 0; i < steps; i++) {
      rope[0] = [
        rope[0][0] + directions[direction][0],
        rope[0][1] + directions[direction][1],
      ];

      // move the other bits of the rope
      for (let j = 1; j < ropeLength; j++) {
        const dx = rope[j - 1][0] - rope[j][0];
        const dy = rope[j - 1][1] - rope[j][1];
        if (Math.abs(dx) > 1) {
          rope[j][0] += dx > 0 ? 1 : -1;
          if (dy != 0) rope[j][1] += dy > 0 ? 1 : -1;
        } else if (Math.abs(dy) > 1) {
          rope[j][1] += dy > 0 ? 1 : -1;
          if (dx != 0) rope[j][0] += dx > 0 ? 1 : -1;
        }
      }
      tailVisited.add(rope[ropeLength - 1].join(","));
      if (visual) {
        drawRope(ctx, rope);
      }
    }
  });
  return tailVisited.size;
};

if (data.length > 0) {
  const part1 = solve(2);
  const part2 = solve(10);
  console.log(`Day 9, part 1: ${part1}, part 2: ${part2}`);
}
