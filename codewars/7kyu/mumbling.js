function accum(s) {
  let str = "";
  const arr = s.split("");
  arr.map((item, index) => {
    str += `${item.toUpperCase()}`;
    for (let i = 0; i < index; i++) {
      str += `${item.toLowerCase()}`;
    }
    if (index !== arr.length - 1) str += `-`;
  });

  return str;
}

accum("ZpglnRxqenU");
