function createPhoneNumber(numbers) {
  const first = numbers.slice(0, 3).toString().replaceAll(",", "");
  const second = numbers.slice(3, 6).toString().replaceAll(",", "");
  const third = numbers.slice(6).toString().replaceAll(",", "");

  return `(${first}) ${second}-${third}`;
}

createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]);
