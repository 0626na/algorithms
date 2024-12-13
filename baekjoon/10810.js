function solution(input) {
  const bucket = [];
  const bucketCount = parseInt(input[0].split(" ")[0]);
  const ballCount = parseInt(input[0].split(" ")[1]);

  for (let index = 0; index < bucketCount; index++) bucket.push(0);

  for (let index = 1; index <= ballCount; index++) {
    const ballAction = input[index].split(" ").map((item) => parseInt(item));

    for (let index = ballAction[0] - 1; index < ballAction[1]; index++)
      bucket[index] = ballAction[ballAction.length - 1];
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
