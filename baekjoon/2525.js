function solution(input) {
  const hour = parseInt(input[0].split(" ")[0]);
  const minute = parseInt(input[0].split(" ")[1]);
  const time = parseInt(input[1]);

  let calHour = hour + parseInt(time / 60);
  let calMinute = minute + parseInt(time % 60);

  if (calMinute >= 60) {
    calMinute = parseInt(calMinute % 60);
    calHour += 1;
  }

  console.log(`${parseInt(calHour % 24)} ${calMinute}`);
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
