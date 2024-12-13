function solution(input) {
  const count = input.shift();
  const quarter = 25;
  const dime = 10;
  const nickel = 5;
  const penny = 1;
  let answer = "";

  input.map((item) => {
    answer = "";
    let temp = +item;
    answer += `${parseInt(temp / quarter).toString()} `;
    temp %= quarter;

    answer += `${parseInt(temp / dime).toString()} `;
    temp %= dime;

    answer += `${parseInt(temp / nickel).toString()} `;
    temp %= nickel;

    answer += `${parseInt(temp / penny).toString()}`;
    console.log(answer);
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
