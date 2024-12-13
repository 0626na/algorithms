/*
 * 기본 2초부터 시작.
 * 1. 각 알파벳에 해당하는 숫자를 확인
 * 2. 숫자를 확인후 2초에 해당 숫자만큼 초를 더한다.
 */

function solution(inputDial) {
  const dials = new Map();
  const arr = [...inputDial];
  let dialNumbers = [];
  let time = 0;

  dials.set("ABC", 2);
  dials.set("DEF", 3);
  dials.set("GHI", 4);
  dials.set("JKL", 5);
  dials.set("MNO", 6);
  dials.set("PQRS", 7);
  dials.set("TUV", 8);
  dials.set("WXYZ", 9);

  arr.map((item) => {
    for (const [key, value] of dials) {
      if ([...key].find((k) => item === k) !== undefined) {
        dialNumbers.push(value);
        break;
      }
    }
  });

  dialNumbers.map((item) => {
    time += item + 1;
  });

  console.log(time);
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
