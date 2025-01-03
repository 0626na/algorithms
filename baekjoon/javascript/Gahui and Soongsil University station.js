function solution(input) {
  let answer = 0;
  const stair = 17;
  const escalator = 21;

  input.map((item) => {
    const arr = item.split(" ");

    if (arr[0] === "Es") {
      answer += arr[1] * escalator;
    }
    if (arr[0] === "Stair") {
      answer += arr[1] * stair;
    }
  });

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
