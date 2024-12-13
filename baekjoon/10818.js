function solution(input) {
  const arr = input[1].split(" ").map((item) => parseInt(item));
  arr.sort((a, b) => a - b);

  console.log(`${arr[0]} ${arr[arr.length - 1]}`);
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
