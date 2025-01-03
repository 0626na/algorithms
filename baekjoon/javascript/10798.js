function solution(input) {
  let maxLength = 0;
  let answer = "";

  input.map((item) => {
    if (item.length > maxLength) maxLength = item.length;
  });

  for (let index = 0; index < maxLength; index++) {
    input.map((item) => {
      if (item.length >= index + 1) answer += [...item.split("")][index];
    });
  }
  console.log(answer);
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
