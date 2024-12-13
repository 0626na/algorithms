function solution(input) {
  const count = parseInt(input[0]);

  for (let index = 1; index <= count; index++) {
    const students = input[index].split(" ").map((item) => parseInt(item));
    const studentsCount = students.shift();
    let sum = 0;

    students.map((item) => (sum += item));

    const average = sum / studentsCount;
    const survivor = students.filter((item) => item > average);

    const result = ((survivor.length / studentsCount) * 100).toFixed(3);

    console.log(`${result}%`);
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
