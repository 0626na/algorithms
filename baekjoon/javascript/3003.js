function solution(pines) {
  const arr = pines.split(" ");
  const pineCount = [1, 1, 2, 2, 2, 8];
  let answer = [];
  pineCount.map((item, index) => {
    if (item === arr[index]) {
      answer.push(0);
      return;
    }
    answer.push(item - arr[index]);
  });

  console.log(answer.join(" "));
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
  solution(input);
  process.exit();
});
