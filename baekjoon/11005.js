function solution(input) {
  let answer = "";
  let value = +input.split(" ")[0];
  const n = +input.split(" ")[1];
  const map = new Map([
    [10, "A"],
    [11, "B"],
    [12, "C"],
    [13, "D"],
    [14, "E"],
    [15, "F"],
    [16, "G"],
    [17, "H"],
    [18, "I"],
    [19, "J"],
    [20, "K"],
    [21, "L"],
    [22, "M"],
    [23, "N"],
    [24, "O"],
    [25, "P"],
    [26, "Q"],
    [27, "R"],
    [28, "S"],
    [29, "T"],
    [30, "U"],
    [31, "V"],
    [32, "W"],
    [33, "X"],
    [34, "Y"],
    [35, "Z"],
  ]);

  while (value !== 0) {
    const temp = value % n;
    map.get(temp) !== undefined
      ? (answer += map.get(temp))
      : (answer += temp.toString());
    value = parseInt(value / n);
  }

  console.log([...answer.split("")].reverse().join(""));
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
