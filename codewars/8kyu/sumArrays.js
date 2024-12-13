// Sum Numbers
function sum(numbers) {
  "use strict";
  let sum = 0;

  if (numbers.length === 0) return sum;
  numbers.map((item) => (sum += item));

  return sum;
}
