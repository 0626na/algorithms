function solution(input) {
  let arr = [];
  let max = 0;
  let loc_row = 1;
  let loc_col = 1;

  input.map((item) => arr.push([...item.split(" ").map((item) => +item)]));
  arr.map((item, row) => {
    item.map((el, col) => {
      if (el > max) {
        max = el;
        loc_row = row + 1;
        loc_col = col + 1;
        return;
      }
      if (el === max) {
        loc_row = row + 1;
        loc_col = col + 1;
      }
    });
  });

  console.log(max);
  console.log(`${loc_row} ${loc_col}`);
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
