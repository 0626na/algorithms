/**
 * @param {BigInt} n
 * @return {BigInt}
 */
function cardGame(n) {
  let alice = 0n;
  let bob = 0n;

  while (n > 0n) {
    console.log(n, alice, bob);
    if (n % 2n === 0n) {
      alice += n / 2n;
      n -= n / 2n;

      if (n === 0n) break;
      if (n % 2n === 0n) {
        bob += n / 2n;
        n -= n / 2n;
      } else {
        bob += 1n;
        n -= 1n;
      }
    } else {
      alice++;
      n--;

      if (n === 0n) break;
      if (n % 2n === 0n) {
        bob += n / 2n;
        n -= n / 2n;
      } else {
        bob++;
        n--;
      }
    }
  }

  console.log("끝나고", alice, bob);
  return alice;
}
