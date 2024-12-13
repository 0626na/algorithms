function solution(input) {
  let sum = 0;
  [...input[1]].map((item) => (sum += parseInt(item)));

  console.log(sum);
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
