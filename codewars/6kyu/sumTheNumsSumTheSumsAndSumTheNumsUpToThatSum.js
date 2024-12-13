function sumOfSums(k) {
  return (S(k) * (S(k) + 1n)) / 2n;
}

const S = (k) => (k * (k + 1n) * (k + 2n)) / 6n;
