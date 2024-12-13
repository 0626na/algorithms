function solution(input) {
  const bucketNumber = parseInt(input[0].split(" ")[0]);
  const count = parseInt(input[0].split(" ")[1]);
  let bucket = [];

  for (let index = 1; index <= bucketNumber; index++) bucket.push(index);

  for (let index = 1; index <= count; index++) {
    const orderArr = input[index].split(" ").map((item) => parseInt(item));
    let temp = 0;

    temp = bucket[orderArr[0] - 1];
    bucket[orderArr[0] - 1] = bucket[orderArr[1] - 1];
    bucket[orderArr[1] - 1] = temp;
  }

  console.log(bucket.join(" "));
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
