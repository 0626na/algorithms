function solution(input) {
  const arr = input[1].split(" ").map((item) => parseInt(item));
  const target = parseInt(input[2]);

  console.log(arr.filter((item) => item === target).length);
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
