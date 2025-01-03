function solution(input) {
  let answer = 1;
  if (input === 0) {
    console.log(answer);
    return;
  }
  for (let index = input; index > 0; index--) {
    answer *= index;
  }

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
