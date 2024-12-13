function alphabetPosition(text) {
  const arr = text.match(/[a-z]/gi);

  if (arr === null) return "";
  const positionArr = arr.map((item) => item.toLowerCase().charCodeAt() - 96);

  return positionArr.join(" ");
}

console.log(alphabetPosition("q@]kg//2"));
