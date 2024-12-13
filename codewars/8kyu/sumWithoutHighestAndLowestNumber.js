function sumArray(array) {
  if (array === null) return 0;
  if (array === undefined) return 0;
  if (array.length <= 1) return 0;
  const arr = array.sort((a, b) => a - b);
  let sum = 0;

  arr.map((item, index) => {
    if (index !== 0 && index !== arr.length - 1) sum += item;
  });

  return sum;
}
