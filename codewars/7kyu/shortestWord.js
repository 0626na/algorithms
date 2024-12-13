function findShort(s) {
  let shortest = 0;
  s.split(" ").map((item) => {
    if (shortest === 0) shortest = item.length;
    shortest > item.length ? (shortest = item.length) : null;
  });

  return shortest;
}

console.log(findShort("nills is cute"));
