function descendingOrder(n) {
  const arr = n.toString().split("");
  const sortedArr = arr.sort((a, b) => b - a);

  return Number(sortedArr.toString().replaceAll(",", ""));
}
