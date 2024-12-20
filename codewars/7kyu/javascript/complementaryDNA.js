function DNAStrand(dna) {
  const arr = [...dna];

  const converted = arr.map((item) => {
    if (item === "A") return "T";
    if (item === "T") return "A";
    if (item === "G") return "C";
    if (item === "C") return "G";
  });

  return converted.join("");
}
