/*
성지키기

문제
영식이는 직사각형 모양의 성을 가지고 있다. 성의 1층은 몇 명의 경비원에 의해서 보호되고 있다. 영식이는 모든 행과 모든 열에 한 명 이상의 경비원이 있으면 좋겠다고 생각했다.

성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 성의 세로 크기 N과 가로 크기 M이 주어진다. N과 M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 성의 상태가 주어진다. 성의 상태는 .은 빈칸, X는 경비원이 있는 칸이다.

출력
첫째 줄에 추가해야 하는 경비원의 최솟값을 출력한다.

예제 입력 1 
4 4
....
....
....
....
예제 출력 1 
4

예제 입력 2 
3 5
XX...
.XX..
...XX
예제 출력 2 
0

예제 입력 3 
5 8
....XXXX
........
XX.X.XX.
........
........
예제 출력 3 
3

출처
문제를 번역한 사람: baekjoon

알고리즘 분류
구현 
 */

const { createInterface } = require("readline");
const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let n = -1;
  let m = -1;
  let castle: (string | null)[][] = [];
  let current = 0; //현재 입력하는 성의 row 위치

  rl.on("line", (input: string) => {
    // 맨처음에 n과 m을 입력해주고 넘어감
    if (n == -1 && m == -1) {
      [n, m] = input.split(" ").map(Number);
      for (let i = 0; i < n; i++) {
        castle[i] = [];
        for (let j = 0; j < m; j++) castle[i][j] = null;
      }
    } else {
      castle[current] = input.split(""); //각 row의 복도 값
      current++; //다음 row로 현재상태 변경

      if (current == n) rl.close(); //n 만큼 전부 row 입력했으면 입력 종료
    }
  }).on("close", () => {
    let missingGuardRowCount = 0;
    let missingGuardColCount = 0;

    //row 방향으로 경비원 숫자 확인
    for (let i = 0; i < n; i++) {
      if (!castle[i].includes("X")) missingGuardRowCount++;
    }

    //column 방향으로 경비원 숫자 확인
    for (let i = 0; i < m; i++) {
      let hasGaurd = false;
      for (let j = 0; j < n; j++) {
        if (castle[j][i] == "X") {
          hasGaurd = true;
          break;
        }
      }

      if (!hasGaurd) missingGuardColCount++;
    }

    console.log(Math.max(missingGuardRowCount, missingGuardColCount));
  });
};

solution();
