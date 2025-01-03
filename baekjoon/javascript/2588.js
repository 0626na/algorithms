function solution(input) {
  const first = parseInt(input[0]);
  const second = parseInt(input[1]);

  const second_firstNumber = parseInt(second / 100);
  const second_secondNumber = parseInt(parseInt(second % 100) / 10);
  const second_thirdNumber = parseInt(parseInt(second % 100) % 10);

  console.log(first * second_thirdNumber);
  console.log(first * second_secondNumber);
  console.log(first * second_firstNumber);
  console.log(first * second);
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
