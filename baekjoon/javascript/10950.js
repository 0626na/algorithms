function solution(input) {
  for (let index = 1; index <= parseInt(input[0]); index++) {
    const arr = input[index].split(" ").map((item) => parseInt(item));

    console.log(arr[0] + arr[1]);
  }
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
