function firstNonConsecutive(arr) {
  let nonConsecutive = null;
  arr.map((item, index) => {
    if (
      index !== arr.length - 1 &&
      arr[index + 1] - item !== 1 &&
      nonConsecutive === null
    ) {
      nonConsecutive = arr[index + 1];
    }
  });

  return nonConsecutive;
}

firstNonConsecutive([1, 2, 3, 4, 6, 7, 8]);
