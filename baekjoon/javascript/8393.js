function solution(input) {
  let sum = 0;
  for (let index = 1; index <= input; index++) {
    sum += index;
  }

  console.log(sum);
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
