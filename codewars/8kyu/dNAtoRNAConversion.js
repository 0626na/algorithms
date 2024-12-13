function DNAtoRNA(dna) {
  const arr = dna.split("");
  const RNA = arr.map((item) => {
    if (item === "T") return "U";

    return item;
  });

  return RNA.toString().replaceAll(",", "");
}
