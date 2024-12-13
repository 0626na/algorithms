function solution(input) {
  const arr = [...input];
  const croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];
  let index = 0;
  let count = 0;

  while (1) {
    if (index > arr.length - 1) break;

    const char2 = `${arr[index]}${arr[index + 1]}`;
    if (!!croatia.find((item) => item === char2)) {
      count++;
      index += 2;
      continue;
    }

    const char3 = `${arr[index]}${arr[index + 1]}${arr[index + 2]}`;
    if (!!croatia.find((item) => item === char3)) {
      count++;
      index += 3;
      continue;
    }

    count++;
    index++;
  }

  console.log(count);
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
