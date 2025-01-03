function solution(input) {
  (input % 4 === 0 && input % 100 !== 0) || input % 400 === 0
    ? console.log("1")
    : console.log("0");
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
