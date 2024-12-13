function longestConsec(strarr, k) {
  let wordLength = 0;
  let longestIndex = 0;
  if (strarr.length < k || k < 0) return "";
  strarr.map((item, index) => {
    let combined = "";

    if (index + k > strarr.length) return;

    for (let i = index; i < index + k; i++) {
      combined += strarr[i];
    }
    if (wordLength < combined.length) {
      wordLength = combined.length;
      longestIndex = index;
    }
  });

  return strarr.slice(longestIndex, longestIndex + k).join("");
}
