function getSum(a, b) {
  let start = 0;
  let end = 0;
  let sum = 0;

  if (a < b) {
    start = a;
    end = b;
  } else {
    start = b;
    end = a;
  }

  for (let index = start; index <= end; index++) {
    sum += index;
  }

  return sum;
}
