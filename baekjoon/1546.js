function solution(input) {
  const count = parseInt(input[0]);
  const scores = input[1]
    .split(" ")
    .map((item) => parseInt(item))
    .sort((a, b) => a - b);
  const max = scores[count - 1];
  const fakeScores = scores.map((item) => (item / max) * 100);

  let sum = 0;
  fakeScores.map((item) => (sum += item));

  console.log(sum / count);
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
