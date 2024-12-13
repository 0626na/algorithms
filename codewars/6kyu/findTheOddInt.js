function findOdd(numbers) {
  const setArr = [...new Set(numbers)];
  let oddItem = 0;
  setArr.map((item) => {
    const odd = numbers.filter((n) => item === n).length;
    if (odd % 2 !== 0) oddItem = item;
  });

  return oddItem;
}
