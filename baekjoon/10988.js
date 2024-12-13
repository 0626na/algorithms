function solution(input) {
  [...input].join("") === [...input].reverse().join("")
    ? console.log(1)
    : console.log(0);
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
