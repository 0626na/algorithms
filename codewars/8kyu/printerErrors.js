function printerError(s) {
  const bottom = s.length;
  const top = s.split("").filter((item) => item.charCodeAt() > 109).length;

  return `${top}/${bottom}`;
}
