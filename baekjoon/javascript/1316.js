function solution(input) {
  const count = input.shift();
  let answer = 0;

  for (let index = 0; index < count; index++) {
    const arr = [...input[index]];
    const set = [...new Set(arr)];
    let firstFound = false;
    let not = false;

    set.map((item) => {
      arr.map((char, index) => {
        if (item === char && !firstFound) {
          firstFound = true;
          return;
        }

        if (
          firstFound &&
          item === char &&
          item !== arr[index - 1] &&
          item !== arr[index + 1]
        ) {
          not = true;
        }
      });
      firstFound = false;
    });
    if (!not) answer++;
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
