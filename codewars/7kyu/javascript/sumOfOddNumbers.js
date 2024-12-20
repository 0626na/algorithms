function rowSumOddNumbers(n) {
  let fisrtElement = 1;
  let sum = 0;

  for (let i = 1; i < n; i++) {
    fisrtElement += i * 2;
  }

  for (let i = 1; i < n; i++) {
    sum += fisrtElement + i * 2;
  }

  return sum + fisrtElement;
}

rowSumOddNumbers(42);
