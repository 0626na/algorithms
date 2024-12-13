function abbrevName(name) {
  const nameArr = name.split(" ");

  const fisrtWord = nameArr[0];
  const secondWord = nameArr[1];

  const firstInitial = fisrtWord.split("")[0].toUpperCase();
  const secondInitial = secondWord.split("")[0].toUpperCase();

  return `${firstInitial}.${secondInitial}`;
}
