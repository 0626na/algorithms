function getMiddle(s) {
  const arr = s.split("");
  let result = "";

  if (arr.length % 2 == 0) {
    return `${arr[arr.length / 2 - 1]}${arr[arr.length / 2]}`;
  }

  return `${arr[Math.floor(arr.length / 2)]}`;
}

getMiddle("testing");
