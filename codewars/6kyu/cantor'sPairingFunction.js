const object = {
  a: 1,
  b: 1,
};

const upStream = () => {
  if (object.a === 1) {
    object.b += 1;
    return;
  }

  object.a -= 1;
  object.b += 1;
};

const downStream = () => {
  if (object.b === 1) {
    object.a += 1;
    return;
  }

  object.a += 1;
  object.b -= 1;
};

function cantor(n) {
  let a = 1;
  let b = 1;

  for (let i = 1; i < n; i++) {
    if (a === 1) b += 1;
  }
}

console.log(cantor(1));
console.log(cantor(2));
console.log(cantor(3));
console.log(cantor(4));
console.log(cantor(5));
