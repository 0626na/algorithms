/*
백준 알고리즘
부호

문제
N개의 정수가 주어지면, 이 정수들의 합 S의 부호를 구하는 프로그램을 작성하시오.

입력
총 3개의 테스트 셋이 주어진다. 각 테스트 셋의 첫째 줄에는 N(1 ≤ N ≤ 100,000)이 주어지고, 둘째 줄부터 N개의 줄에 걸쳐 각 정수가 주어진다. 주어지는 정수의 절댓값은 9223372036854775807보다 작거나 같다.

출력
총 3개의 줄에 걸쳐 각 테스트 셋에 대해 N개의 정수들의 합 S의 부호를 출력한다. S=0이면 "0"을, S>0이면 "+"를, S<0이면 "-"를 출력하면 된다.

예제 입력 1 
3
0
0
0
10
1
2
4
8
16
32
64
128
256
-512
6
9223372036854775807
9223372036854775806
9223372036854775805
-9223372036854775807
-9223372036854775806
-9223372036854775804

예제 출력 1 
0
-
+

출처
문제를 만든 사람: author5
빠진 조건을 찾은 사람: joonas, pichulia
데이터를 추가한 사람: ntopia
문제의 오타를 찾은 사람: ZZangZZang

알고리즘 분류
수학
사칙연산
임의 정밀도 / 큰 수 연산
 */

// async await 방식

// const solution = async () => {
//   let count = 3;
//   let result = [];

//   for (let i = 1; i <= count; i++) {
//     const n = parseInt(await rl.question(""));
//     let sum = 0n;

//     for (let j = 1; j <= n; j++) {
//       const num = BigInt(await rl.question(""));
//       sum += num;
//     }

//     if (sum == 0) result.push("0");
//     else if (sum > 0) result.push("+");
//     else result.push("-");
//   }

//   for (const item of result) {
//     console.log(item);
//   }

//   rl.close();

//   rl.on("close", () => {
//     process.exit(0);
//   });
// };

const { createInterface } = require("readline");
const { stdin: input, stdout: output } = require("process");

const rl = createInterface({ input, output });

const solution = () => {
  let result = [];
  const count = 3;
  let current = 0;
  let next = true;
  let n = 0;
  let sum = 0n;

  rl.on("line", (input) => {
    // 각 테스트마다 첫번째 입력. 입력할 갯수를 입력
    if (next) {
      n = parseInt(input);
      sum = 0n;
      next = false;
    } else {
      sum += BigInt(input);
      n--;

      // 합 확인
      if (n == 0) {
        if (sum == 0) result.push("0");
        else if (sum > 0) result.push("+");
        else result.push("-");
        next = true;
        current++;

        // 총 세번의 테스트이므로 테스트를 다 했는지를 확인
        if (current == count) {
          rl.close();
        }
      }
    }
  }).on("close", () => {
    result.forEach((item) => console.log(item));
    process.exit(0);
  });
};

solution();
