var number = function (busStops) {
  const arr = busStops.flatMap((item) => item);
  let droppedPeople = 0;
  let onTheBusPeople = 0;

  arr.map((item, index) => {
    if (index % 2 === 0) onTheBusPeople += item;
    else droppedPeople += item;
  });

  return onTheBusPeople - droppedPeople;
};
