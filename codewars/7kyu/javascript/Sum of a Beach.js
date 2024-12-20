/**
 * codewars 7kyu 문제 Sum of a Beach. string, regular expressions
 *
 * Beaches are filled with sand, water, fish, and sun.
 * Given a string,
 *
 * calculate how many times the words "Sand", "Water", "Fish", and "Sun" appear without overlapping (regardless of the case).
 */
function sumOfABeach(beach) {
  const rex = /(sand|water|fish|sun)/i;
  const t = beach.match(rex);
  return !beach.match(rex) ? 0 : beach.match(rex).length;
}

console.log(
  sumOfABeach(
    "joifjepiojfoiejfoajoijawoeifjowejfjoiwaefjiaowefjaofjwoj fawojef"
  )
);
