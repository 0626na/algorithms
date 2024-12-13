function solution(input) {
  let max = 0;
  let maxIndex = 0;
  input.map((item, index) => {
    if (parseInt(item) > max) {
      max = item;
      maxIndex = index;
    }
  });

  console.log(max);
  console.log(maxIndex + 1);
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
