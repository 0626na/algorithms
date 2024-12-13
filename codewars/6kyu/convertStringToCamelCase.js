function toCamelCase(str) {
  if (str.split("-").length === 1 && str.split("_").length === 1) return str;

  str.split("-").length !== 1 ? (stand = "-") : (stand = "_");
  const arr = str.split(/[-|_]/);
  const converted = arr.map((item, index) => {
    const element = [...item];
    if (index !== 0) element.splice(0, 1, element[0].toUpperCase());

    return element.join("");
  });

  return converted.join("");
}

toCamelCase("the_catWas-Pippi");
