function isPangram(string) {
  let result = true;
  let checkArr = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
  ];

  [
    ...string
      .toLowerCase()
      .replaceAll(".", "")
      .replaceAll(/[0-9]/g, "")
      .replaceAll(" ", ""),
  ].map((item) => {
    if (checkArr.findIndex((character) => character === item) !== -1)
      checkArr.splice(
        checkArr.findIndex((character) => character === item),
        1
      );
  });

  return checkArr.length === 0 ? true : false;
}

isPangram("aaaaaaaaaaaaaaaaaaaaaaaaaa");
