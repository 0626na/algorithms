/*
백준 알고리즘 1267번
핸드폰 요금

문제
동호는 새악대로 T 통신사의 새 핸드폰 옴머나를 샀다. 새악대로 T 통신사는 동호에게 다음 두 가지 요금제 중 하나를 선택하라고 했다.

1. 영식 요금제
2. 민식 요금제
영식 요금제는 30초마다 10원씩 청구된다. 이 말은 만약 29초 또는 그 보다 적은 시간 통화를 했으면 10원이 청구된다. 만약 30초부터 59초 사이로 통화를 했으면 20원이 청구된다.

민식 요금제는 60초마다 15원씩 청구된다. 이 말은 만약 59초 또는 그 보다 적은 시간 통화를 했으면 15원이 청구된다. 만약 60초부터 119초 사이로 통화를 했으면 30원이 청구된다.

동호가 저번 달에 새악대로 T 통신사를 이용할 때 통화 시간 목록이 주어지면 어느 요금제를 사용 하는 것이 저렴한지 출력하는 프로그램을 작성하시오.

입력
동호가 저번 달에 이용한 통화의 개수 N이 주어진다. N은 20보다 작거나 같은 자연수이다. 둘째 줄에 통화 시간 N개가 주어진다. 통화 시간은 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 싼 요금제의 이름을 출력한다. 그 후에 공백을 사이에 두고 요금이 몇 원 나오는지 출력한다. 만약 두 요금제의 요금이 모두 같으면 영식을 먼저 쓰고 민식을 그 다음에 쓴다.

영식은 Y로, 민식은 M으로 출력한다.

예제 입력 1 
3
40 40 40
예제 출력 1 
M 45
영식: 20 + 20 + 20 = 60
민식: 15 + 15 + 15 = 45

예제 입력 2 
3
61 61 61
예제 출력 2 
Y M 90

예제 입력 3 
2
61 10
예제 출력 3 
Y 40
영식: 30 + 10 = 40
민식: 30 + 15 = 45

예제 입력 4 
2
60 65
예제 출력 4 
Y M 60
영식: 30 + 30 = 60
민식: 30 + 30 = 60

출처
ICPC > Regionals > Asia Pacific > Malaysia > Asia Regional 2008 - Kuala Lumpur C번

문제를 번역한 사람: baekjoon
데이터를 추가한 사람: doju
빠진 조건을 찾은 사람: gilsu91, jane22th, nisroeld99, purpose, skynet
문제의 오타를 찾은 사람: gumgood, mwy3055, waylight3

알고리즘 분류
수학
사칙연산
 */

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const solution = () => {
  let n = 0;

  rl.on("line", (input) => {
    if (n == 0) n = parseInt(input);
    else {
      const times = input.split(" ");
      let yongsik = 0;
      let minsik = 0;

      times.forEach((item) => {
        const time = parseInt(item);
        yongsik += Math.floor(time / 30) * 10 + 10;
        minsik += Math.floor(time / 60) * 15 + 15;
      });

      if (yongsik > minsik) console.log("M", minsik);
      else if (yongsik == minsik) console.log("Y M", yongsik);
      else console.log("Y", yongsik);

      rl.close();
    }
  }).on("close", () => {
    process.exit(0);
  });
};

solution();
