function bouncingBall(h, bounce, window) {
  if (h < 0 || bounce <= 0 || bounce >= 1 || window >= h) return -1;

  let count = 1;
  let bouncedHeight = 0;

  while (1) {
    if (bouncedHeight === 0) {
      bouncedHeight = h * bounce;
    } else {
      bouncedHeight = bouncedHeight * bounce;
    }

    if (window > bouncedHeight && bouncedHeight !== 0) break;

    if (window < bouncedHeight) count += 2;
  }

  return count;
}

console.log(bouncingBall(10, 0.6, 10));
