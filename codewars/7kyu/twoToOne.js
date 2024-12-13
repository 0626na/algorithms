function longest(s1, s2) {
  const s1Set = new Set(s1.split(""));
  const s2Set = new Set(s2.split(""));
  const combinedArr = [...s1Set, ...s2Set];
  const combinedSet = new Set(combinedArr);
  const sortedArr = [...combinedSet].sort();
  const convertedString = sortedArr.toString().replaceAll(",", "");
  return convertedString;
}
