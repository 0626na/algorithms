function removeSmallest(numbers) {
  const innerNumbers = [...numbers];
  const min = Math.min(...innerNumbers);

  innerNumbers.splice(
    innerNumbers.findIndex((item) => item === min),
    1
  );

  return innerNumbers;
}
