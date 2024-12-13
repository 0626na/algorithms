function high(x) {
  const arr = x.split(" ");
  let highestScoreWordIndex = 0;
  let highestScore = 0;

  arr.map((item, index) => {
    let temp = 0;
    item.split("").map((i) => {
      temp += i.charCodeAt() - 96; //아스키코드 변환
    });

    if (highestScore < temp) {
      highestScore = temp;
      highestScoreWordIndex = index;
    }
  });

  return arr[highestScoreWordIndex];
}
