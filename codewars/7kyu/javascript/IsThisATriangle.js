function isTriangle(a, b, c) {
  const arr = [a, b, c].sort((i, j) => i - j);

  return arr[2] < arr[0] + arr[1];
}

isTriangle(10, -1, 4);
