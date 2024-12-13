const zeroFuel = (distanceToPump, mpg, fuelLeft) => {
  const distance = mpg * fuelLeft;

  return distanceToPump <= distance;
};
