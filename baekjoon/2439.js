function solution(input) {
  for (let index = 0; index < input; index++) {
    let star = "";
    for (let item = input; item > index + 1; item--) star += " ";

    for (let number = 0; number <= index; number++) star += "*";

    console.log(star);
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
