function solution(input) {
  const count = parseInt(input[0]);

  input.map((item, index) => {
    if (index === 0) return;

    const arr = item.split(" ");
    const repeatCount = parseInt(arr[0]);
    let str = "";
    [...arr[1]].map((item) => {
      for (let index = 0; index < repeatCount; index++) str += item;
    });
    console.log(str);
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
  solution(input);
  process.exit();
});
