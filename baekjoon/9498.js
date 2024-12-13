function solution(input) {
  if (90 <= input && input <= 100) {
    console.log("A");
    return;
  }
  if (80 <= input && input <= 89) {
    console.log("B");
    return;
  }

  if (70 <= input && input <= 79) {
    console.log("C");
    return;
  }

  if (60 <= input && input <= 69) {
    console.log("D");
    return;
  }

  console.log("F");
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
