function oddOrEven(array) {
  return array.reduce((acc, item) => acc + item, 0) % 2 == 0 ? "even" : "odd";
}
