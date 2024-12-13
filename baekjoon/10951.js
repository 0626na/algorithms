function solution(input) {
  const count = input.length;

  for (let index = 0; index < count; index++) {
    console.log(
      parseInt(input[index].split(" ")[0]) +
        parseInt(input[index].split(" ")[1])
    );
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
