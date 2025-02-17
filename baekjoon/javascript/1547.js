/*
 백준 알고리즘 1547번
공

문제
세준이는 컵 3개를 탁자 위에 일렬로 엎어놓았다. 컵의 번호는 맨 왼쪽 컵부터 순서대로 1번, 2번 3번이고, 세준이는 이 컵을 이용해서 게임을 하려고 한다.

먼저 1번 컵의 아래에 공을 하나 넣는다. 세준이는 두 컵을 고른 다음, 그 위치를 맞바꾸려고 한다. 예를 들어, 고른 컵이 1번과 2번이라면, 1번 컵이 있던 위치에 2번 컵을 이동시키고, 동시에 2번 컵이 있던 위치에 1번 컵을 이동시켜야 한다. 이때 공은 움직이지 않기 때문에, 공의 위치는 맨 처음 1번 컵이 있던 위치와 같다.

세준이는 컵의 위치를 총 M번 바꿀 것이며, 컵의 위치를 바꾼 방법이 입력으로 주어진다. 위치를 M번 바꾼 이후에 공이 들어있는 컵의 번호를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 컵의 위치를 바꾼 횟수 M이 주어지며, M은 50보다 작거나 같은 자연수이다. 둘째 줄부터 M개의 줄에는 컵의 위치를 바꾼 방법 X와 Y가 주어지며, X번 컵과 Y번 컵의 위치를 서로 바꾸는 것을 의미한다. X와 Y의 값은 3보다 작거나 같고, X와 Y가 같을 수도 있다.

컵을 이동시킨 후에 공이 컵 바깥에 있는 경우는 없다.

출력
첫째 줄에 공이 들어있는 컵의 번호를 출력한다. 공이 사라져서 컵 밑에 없는 경우에는 -1을 출력한다.

예제 입력 1 
4
3 1
2 3
3 1
3 2
예제 출력 1 
3

예제 입력 2 
2
1 2
3 1
예제 출력 2 
2

예제 입력 3 
5
2 3
1 3
2 3
2 1
3 1
예제 출력 3 
3

예제 입력 4 
9
1 2
3 2
1 2
2 1
2 1
3 2
1 3
3 1
1 2
예제 출력 4 
1
출처

어색한 표현을 찾은 사람: BaaaaaaaaaaarkingDog, friendof865
문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: hwonjoon
문제를 다시 작성한 사람: jh05013

알고리즘 분류
구현
시뮬레이션
 */

const { createInterface } = require("readline");
const rl = createInterface({ input: process.stdin, output: process.stdout });

const solution = () => {
  let m = 0,
    current = 0,
    ballPosition = 1;

  rl.on("line", (input) => {
    if (m == 0) {
      m = parseInt(input);
    } else {
      const [a, b] = input.split(" ");
      cupA = parseInt(a);
      cupB = parseInt(b);

      if (cupA == ballPosition) ballPosition = cupB;
      else if (cupB == ballPosition) ballPosition = cupA;

      current++;
      if (current == m) rl.close();
    }
  }).on("close", () => {
    console.log(ballPosition);
    process.exit(0);
  });
};

solution();
