function keepOrder(ary, val) {
  let location = 0;

  ary.map((item, index) => {
    if (item < val) {
      location = index + 1;
    }
  });

  if (ary[ary.length - 1] < val) location = ary.length;
  if (ary[0] > val) location = 0;

  return location;
}
