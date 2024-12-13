function solution(input) {
  for (let index = 1; index < 10; index++) {
    console.log(`${input} * ${index} = ${input * index}`);
  }
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
