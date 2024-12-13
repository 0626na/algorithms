function nbYear(p0, percent, aug, p) {
  let population = 0;
  let year = 0;

  while (1) {
    if (population >= p) break;
    if (year === 0) {
      population = p0 + p0 * (percent / 100) + aug;
      year++;
      continue;
    }

    population = Math.floor(population + population * (percent / 100) + aug);
    year++;
  }

  console.log(year, "년", population);

  return year;
}

console.log(nbYear(1000, 2, 50, 1200));
