function solution(input) {
  const totalAmount = parseInt(input[0]);
  const stuffKind = parseInt(input[1]);
  let check = 0;

  for (let index = 2; index < stuffKind + 2; index++) {
    const amount = parseInt(input[index].split(" ")[0]);
    const count = parseInt(input[index].split(" ")[1]);
    check += amount * count;
  }

  totalAmount === check ? console.log("Yes") : console.log("No");
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
