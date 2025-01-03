function solution(input) {
  for (let index = 0; index < input; index++) {
    let star = "";
    for (let item = 0; item <= index; item++) {
      star += "*";
    }
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
