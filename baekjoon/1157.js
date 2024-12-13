function solution(input) {
  const map = new Map();

  [...input.toUpperCase()].map((item) => map.set(item, 0));

  [...input.toUpperCase()].map((item) => {
    if (map.has(item)) map.set(item, map.get(item) + 1);
  });

  const charCountArr = [...map.values()].sort((a, b) => b - a);
  if (charCountArr.length === 1) {
    console.log(input.toUpperCase());
    return;
  }
  if (charCountArr[0] === charCountArr[1]) {
    console.log("?");
    return;
  }

  [...map.keys()].some((item) => {
    if (map.get(item) === charCountArr[0]) {
      console.log(item);
      return;
    }
  });
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
