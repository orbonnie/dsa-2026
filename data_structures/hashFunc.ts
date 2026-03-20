function naiveHash(key: string, len: number) {
  let sum = 0;

  for(let char of key) {
    let val = char.charCodeAt(0) - 96;
    sum += val;
  }

  return sum % len;
}

function hash(key: any, len: number) {
  let sum = 0;
  let PRIME = 31;

  for (let i = 0; i < Math.min(key.length, 100); i++) {
    let char = key[i];
    let value = char.charCodeAt(0) - 96;
    sum = (sum * PRIME + value);
  }
  return sum % len;
}

console.log(naiveHash("friend", 13));
console.log(naiveHash("flowers", 13));
console.log(naiveHash("communication", 13));
console.log(naiveHash("duck", 13));
console.log(naiveHash("opal", 13));
console.log("******************")
console.log(hash("friend", 13));
console.log(hash("flowers", 13));
console.log(hash("communication", 13));
console.log(hash("duck", 13));
console.log(hash("opal", 13));
