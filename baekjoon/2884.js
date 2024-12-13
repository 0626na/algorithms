function solution(input) {
  let hour = input[0];
  let minute = input[1];

  if (minute - 45 < 0) {
    minute = minute + 15;
    hour - 1 < 0 ? (hour = 23) : (hour -= 1);

    console.log(`${hour} ${minute}`);
  } else {
    minute -= 45;
    console.log(`${hour} ${minute}`);
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
  const list = input.split(" ").map((item) => parseInt(item));
  solution(list);
  process.exit();
});
