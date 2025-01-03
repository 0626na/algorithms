function solution(input) {
  console.log((input[0] + input[1]) % input[2]);
  console.log(((input[0] % input[2]) + (input[1] % input[2])) % input[2]);
  console.log((input[0] * input[1]) % input[2]);
  console.log(((input[0] % input[2]) * (input[1] % input[2])) % input[2]);
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
