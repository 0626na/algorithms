//return the total number of smiling faces in the array
function countSmileys(arr) {
  let count = 0;
  arr.map((item) => {
    if ([...item].length < 4) {
      if ([...item].length === 3) {
        [...item].findIndex((item) => item === ":" || item === ";") !== -1 &&
        [...item].findIndex((item) => item === "~" || item === "-") !== -1 &&
        [...item].findIndex((item) => item === ")" || item === "D") !== -1
          ? count++
          : null;
      }

      if ([...item].length === 2) {
        [...item].findIndex((item) => item === ":" || item === ";") !== -1 &&
        [...item].findIndex((item) => item === ")" || item === "D") !== -1
          ? count++
          : null;
      }
    }
  });

  return count;
}

console.log(countSmileys([":>", ";)", ":~)", ";>", ":->", ":)", ";)"]));
