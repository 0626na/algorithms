function solution(list) {
  if (list[0] < list[1]) {
    console.log("<");
    return;
  }

  if (list[0] > list[1]) {
    console.log(">");
    return;
  }

  console.log("==");
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
  list = input.split(" ").map((el) => parseInt(el));
  solution(list);
  process.exit();
});
