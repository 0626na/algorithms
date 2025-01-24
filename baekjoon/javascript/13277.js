/*
 백준 알고리즘
 큰 수 곱셈

문제
두 정수 A와 B가 주어졌을 때, 두 수의 곱을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 A와 B가 주어진다. 두 정수는 0보다 크거나 같은 정수이며, 0을 제외한 정수는 0으로 시작하지 않으며, 수의 앞에 불필요한 0이 있는 경우도 없다. 또한, 수의 길이는 300,000자리를 넘지 않는다.

출력
두 수의 곱을 출력한다.

예제 입력 1 
1 2
예제 출력 1 
2

예제 입력 2 
3 4
예제 출력 2 
12

예제 입력 3 
893724358493284 238947328947329
예제 출력 3 
213553048277135320552236238436

출처
문제를 만든 사람: baekjoon
문제의 오타를 찾은 사람: wijae

알고리즘 분류
수학
사칙연산
임의 정밀도 / 큰 수 연산

*/

const { stdin: input, stdout: output } = require("process");
const readline = require("readline");

const rl = readline.createInterface({ input, output });

const bigNumberMultiple = () => {
  rl.on("line", (input) => {
    const [a, b] = input.trim().split(" ");
    console.log((BigInt(a) * BigInt(b)).toString());

    rl.close();
  }).on("close", () => {
    process.exit(0);
  });
};

bigNumberMultiple();
