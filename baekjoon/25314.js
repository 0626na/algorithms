function solution(input) {
  let str = "";
  for (let index = 0; index < input; index += 4) {
    str += "long ";
  }
  str += "int";

  console.log(str);
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
