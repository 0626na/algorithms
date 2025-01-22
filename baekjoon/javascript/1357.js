/**
 *
 * 백준
 * 뒤집힌 덧셈
 *
 * 문제
 * 어떤 수 X가 주어졌을 때, X의 모든 자리수가 역순이 된 수를 얻을 수 있다. Rev(X)를 X의 모든 자리수를 역순으로 만드는 함수라고 하자. 예를 들어, X=123일 때, Rev(X) = 321이다. 그리고, X=100일 때, Rev(X) = 1이다.
 * 두 양의 정수 X와 Y가 주어졌을 때, Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오
 *
 * 입력
 * 첫째 줄에 수 X와 Y가 주어진다. X와 Y는 1,000보다 작거나 같은 자연수이다.
 *
 * 출력
 * 첫째 줄에 문제의 정답을 출력한다.
 *
 * 예제 입력 1
 * 123 100
 * 예제 출력 1
 * 223
 * 예제 입력 2
 * 111 111
 * 예제 출력 2
 * 222
 * 예제 입력 3
 * 5 5
 * 예제 출력 3
 * 1
 * 예제 입력 4
 * 1000 1
 * 예제 출력 4
 * 2
 * 예제 입력 5
 * 456 789
 * 예제 출력 5
 * 1461
 *
 * 출처
 * 문제를 번역한 사람: baekjoon
 *
 * 알고리즘 분류
 * 구현
 * 문자열
 *
 **/

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const reversedAdd = () => {
  let input = [];
  let sum = 0;

  rl.on("line", function (line) {
    input = line.trim().split(" ");
    rl.close();
  }).on("close", () => {
    const [x, y] = input;
    const reversedX = x.split("");
    const reversedY = y.split("");
    reversedX.reverse();
    reversedY.reverse();

    sum = `${Number(reversedX.join("")) + Number(reversedY.join(""))}`.split(
      ""
    );
    sum.reverse();

    console.log(parseInt(sum.join("")));
    process.exit();
  });
};

reversedAdd();
