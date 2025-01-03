function solution(input) {
  for (let i = 1; i <= input; i++) {
    let str = "";

    for (let j = 1; j <= input - i; j++) str += " ";
    for (let k = 1; k <= input - (input - i); k++) str += "*";
    for (let n = 1; n < i; n++) str += "*";
    console.log(str);
  }

  for (let i = input - 1; i > 0; i--) {
    let str = "";

    for (let j = 1; j <= input - i; j++) str += " ";
    for (let k = 1; k <= input - (input - i); k++) str += "*";
    for (let n = 1; n < i; n++) str += "*";
    console.log(str);
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
