function solution(input) {
  const value = input.split(" ")[0];
  const arr = [...value.split("")].reverse();
  const n = +input.split(" ")[1];
  let answer = 0;
  const map = new Map([
    ["A", 10],
    ["B", 11],
    ["C", 12],
    ["D", 13],
    ["E", 14],
    ["F", 15],
    ["G", 16],
    ["H", 17],
    ["I", 18],
    ["J", 19],
    ["K", 20],
    ["L", 21],
    ["M", 22],
    ["N", 23],
    ["O", 24],
    ["P", 25],
    ["Q", 26],
    ["R", 27],
    ["S", 28],
    ["T", 29],
    ["U", 30],
    ["V", 31],
    ["W", 32],
    ["X", 33],
    ["Y", 34],
    ["Z", 35],
  ]);

  arr.map((item, index) => {
    if (!!map.get(item)) {
      answer += map.get(item) * n ** index;
    } else {
      answer += +item * n ** index;
    }
  });

  console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input;
rl.on("line", function (line) {
  input = line;
}).on("close", function () {
  solution(input);
  process.exit();
});
