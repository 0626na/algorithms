function solution(input) {
  let arr = [];
  const count = parseInt(input[0].split(" ")[1]);

  for (let index = 1; index <= parseInt(input[0].split(" ")[0]); index++)
    arr.push(index);

  for (let index = 1; index <= count; index++) {
    let temp = [];
    const start = parseInt(input[index].split(" ")[0]) - 1;
    const end = parseInt(input[index].split(" ")[1]);

    for (let index = start; index < end; index++) temp.push(arr[index]);

    temp.reverse();
    let tempIndex = 0;
    arr = arr.map((item, index) => {
      if (start <= index && index < end) {
        const tempItem = temp[tempIndex];
        tempIndex++;
        return tempItem;
      } else return item;
    });
  }

  console.log(arr.join(" "));
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
