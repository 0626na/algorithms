function solution(input) {
  const arr = input.split(" ");
  const number1 = parseInt([...arr[0]].reverse().join(""));
  const number2 = parseInt([...arr[1]].reverse().join(""));

  number1 > number2 ? console.log(number1) : console.log(number2);
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
