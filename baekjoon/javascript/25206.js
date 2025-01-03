function solution(input) {
  let univScoreSum = 0;
  let majorScoreSum = 0;

  input.map((item) => {
    const scores = item.split(" ");
    if (scores[2] !== "P") univScoreSum += Number(scores[1]);

    if (scores[2] === "A+") {
      majorScoreSum += Number(scores[1]) * 4.5;
    }
    if (scores[2] === "A0") {
      majorScoreSum += Number(scores[1]) * 4.0;
    }
    if (scores[2] === "B+") {
      majorScoreSum += Number(scores[1]) * 3.5;
    }
    if (scores[2] === "B0") {
      majorScoreSum += Number(scores[1]) * 3.0;
    }
    if (scores[2] === "C+") {
      majorScoreSum += Number(scores[1]) * 2.5;
    }
    if (scores[2] === "C0") {
      majorScoreSum += Number(scores[1]) * 2.0;
    }
    if (scores[2] === "D+") {
      majorScoreSum += Number(scores[1]) * 1.5;
    }
    if (scores[2] === "D0") {
      majorScoreSum += Number(scores[1]) * 1.0;
    }
    if (scores[2] === "F") {
      majorScoreSum += Number(scores[1]) * 0.0;
    }
  });

  console.log(majorScoreSum / univScoreSum);
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
