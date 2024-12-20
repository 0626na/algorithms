function disemvowel(str) {
  const clean = [...str].filter(
    (item) =>
      item !== "a" &&
      item !== "A" &&
      item !== "i" &&
      item !== "I" &&
      item !== "o" &&
      item !== "O" &&
      item !== "e" &&
      item !== "E" &&
      item !== "u" &&
      item !== "U"
  );

  console.log(clean.toString());
  return clean.toString();
}

disemvowel("ThIs website is for losers LOL!");
