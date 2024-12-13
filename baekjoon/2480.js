function solution(input) {
  const arr = input.sort((a, b) => a - b);

  if (arr[0] === arr[1] && arr[1] === arr[2] && arr[0] === arr[2])
    console.log(10000 + input[0] * 1000);

  if (arr[0] !== arr[1] && arr[1] !== arr[2] && arr[0] !== arr[2])
    console.log(arr[2] * 100);

  if (arr[0] === arr[1] && arr[1] !== arr[2]) console.log(1000 + arr[0] * 100);
  if (arr[1] === arr[2] && arr[0] !== arr[1]) console.log(1000 + arr[1] * 100);
  if (arr[0] === arr[2] && arr[1] !== arr[2]) console.log(1000 + arr[0] * 100);
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
  solution(input.split(" ").map((item) => parseInt(item)));
  process.exit();
});
