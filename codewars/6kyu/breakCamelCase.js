function solution(str) {
  const arr = [...str];
  let camelArr = [];

  arr.map((item) => {
    if (item.match(/[A-Z]/)) camelArr.push(" ");
    camelArr.push(item);
  });

  return camelArr.join("");
}
