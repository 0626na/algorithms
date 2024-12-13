function count(string) {
  const arr = [...string];
  const obj = {};
  arr.map((item) => {
    obj[item] = arr.filter((ch) => ch === item).length;
  });

  return obj;
}
