function solution(input) {
  input.map((item, index) => {
    if (index === 0) return;
    console.log(`${item[0]}${item[item.length - 1]}`);
  });
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
