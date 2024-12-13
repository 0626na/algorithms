function betterThanAverage(classPoints, yourPoints) {
  const average =
    classPoints.reduce((acc, current) => acc + current, 0) / classPoints.length;

  return average < yourPoints;
}
