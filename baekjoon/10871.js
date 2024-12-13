function solution(input) {
  const target = parseInt(input[0].split(" ")[1]);
  const arr = input[1].split(" ").map((item) => parseInt(item));
  const result = arr.filter((item) => item < target);

  console.log(result.join(" "));
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
