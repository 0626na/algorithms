function deleteNth(arr, n) {
  let result = [];
  if (n === 1) return [...new Set(arr)];

  arr.map((item) => {
    let count = 0;
    result.map((element) => {
      if (element === item) count++;
    });

    if (count < n) result.push(item);
  });

  return result;
}

deleteNth([20, 37, 20, 21], 2);
