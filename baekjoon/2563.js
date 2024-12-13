function solution(input) {
  let answer = 0;
  let arr = new Array(100).fill(0);
  arr = arr.map(() => new Array(100).fill(0));
  input.shift();

  input.map((item) => {
    const x = +item.split(" ")[0];
    const y = +item.split(" ")[1];

    for (let i = x - 1; i < x + 9; i++) {
      for (let j = y - 1; j < y + 9; j++) arr[i][j] = 1;
    }
  });

  arr.map((item) => {
    item.map((el) => {
      if (el === 1) answer++;
    });
  });

  console.log(answer);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input = [];
rl.on("line", function (line) {
  input.push(line);
}).on("close", function () {
  solution(input);
  process.exit();
});
