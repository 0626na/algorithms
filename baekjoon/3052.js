function solution(input) {
  const arr = input.map((item) => parseInt(item) % 42);

  console.log([...new Set(arr)].length);
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
