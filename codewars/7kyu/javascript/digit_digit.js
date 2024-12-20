function squareDigits(num) {
  const arr = num.toString().split("");
  const squareArr = arr.map((item) => Number(item) * Number(item));

  return Number(squareArr.toString().replaceAll(",", ""));
}

squareDigits(3212);
