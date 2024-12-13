function solution(input) {
  let answer = "";
  for (let index = 1; index <= input; index++) answer += `${index}\n`;
  console.log(answer);
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
