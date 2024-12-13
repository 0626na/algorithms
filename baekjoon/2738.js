function solution(input) {
  const counts = input.shift();
  let firstArr = [];
  let resultArr = [];

  input[0].map((item, index) => {
    const first = item.split(" ").map((item) => +item);
    const second = input[1][index].split(" ").map((item) => +item);

    first.map((item, index) => resultArr.push(item + second[index]));
    console.log(resultArr.join(" "));
    resultArr = [];
  });
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
  const count = +input[0].split(" ")[0];
  let first = [];
  let second = [];
  for (let index = 1; index <= count; index++) first.push(input[index]);
  for (let index = count + 1; index <= input.length - 1; index++)
    second.push(input[index]);

  const arr = [input[0], first, second];
  solution(arr);
  process.exit();
});
