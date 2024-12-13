function duplicateCount(text) {
  let count = 0;
  let checkedArr = [...text.toLowerCase()];

  [...text.toLowerCase()].map((item) => {
    let temp = 0;

    checkedArr.map((ch) => {
      if (ch === item) temp++;
    });
    if (temp > 1) {
      count++;
      checkedArr = checkedArr.filter((element) => item !== element);
    }
  });

  return count;
}

console.log(duplicateCount("Aa0BC0"));
