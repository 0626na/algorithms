function highAndLow(numbers) {
  const arr = numbers.split(" ");

  const sortedArr = arr.sort((a, b) => a - b);

  return `${sortedArr[sortedArr.length - 1]} ${sortedArr[0]}`;
}
