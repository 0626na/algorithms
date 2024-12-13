function solution(list) {
  console.log(list[0] + list[1] + list[2]);
}

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let input;
let list = [];
rl.on("line", function (line) {
  input = line;
  rl.close();
}).on("close", function () {
  list = input.split(" ").map((el) => el);
  list = input.split(" ").map((el) => parseInt(el)); // 입력값이 정수라면 parseInt로 형 변환
  solution(list);
  process.exit();
});
