function solution(input) {
  let answer = 0;
  let dots = 2;

  for (let index = 1; index <= input; index++) dots += dots - 1;

  answer = dots ** 2;

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
  solution(parseInt(input));
  process.exit();
});
