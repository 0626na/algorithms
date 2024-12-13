function comp(array1, array2) {
  if (array1 === null || array2 === null) return false;

  let arr1 = array1.sort((a, b) => a - b);
  let arr2 = array2.sort((a, b) => a - b);
  let result = true;

  arr1.map((item, index) => {
    if (item !== Math.sqrt(arr2[index])) result = false;
  });

  return result;
}

console.log(comp([121, 144, 19, 161, 19, 144, 19, 11]));
