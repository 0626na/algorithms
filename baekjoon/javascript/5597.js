function solution(input) {
  const arr = input.map((item) => parseInt(item));
  let students = [];
  let n = 1;
  while (students.length !== 2) {
    arr.filter((item) => item === n).length === 0 ? students.push(n) : null;
    n++;
  }

  console.log(students[0]);
  console.log(students[1]);
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
