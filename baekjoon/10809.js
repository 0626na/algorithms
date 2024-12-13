function solution(input) {
  const arr = [...input];
  let result = [];

  for (let index = 97; index <= 122; index++) {
    const ch = String.fromCharCode(index);
    let finded = false;
    arr.some((item, index) => {
      if (item === ch) {
        result.push(index);
        finded = true;
        return true;
      }
    });
    !finded ? result.push(-1) : null;
  }

  console.log(result.join(" "));
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
