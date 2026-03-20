class HashTable {
  keyMap:([string, any][] | undefined)[];

  constructor(size: number = 53) {
    this.keyMap = new Array(size);
  }

  _hash(key: string) {
    let sum = 0;
    let PRIME = 29;

    for(let i = 0; i < Math.min(key.length, 100); i++) {
      let char = key[i];
      let value = char.charCodeAt(0) - 96
      sum = sum * PRIME + value
    }
    return sum % this.keyMap.length;
  }

  set(key: string, value: any) {
    const index = this._hash(key);
    const item: [string, any] = [key, value];
    let bucket = this.keyMap[index];

    if(Array.isArray(bucket)) {
      const existing = bucket.find(tuple => tuple[0] === key);
      if(existing) {
        existing[1] = value;
      } else {
        bucket.push(item);
      }
    } else {
       this.keyMap[index] = [item];
    }
  }

  get(key: string) {
    const index = this._hash(key);
    const bucket = this.keyMap[index];

    if(!bucket) return;

    for(let item of bucket) {
      if(item[0] === key) return item;
    }
    return;
  }

  keys() {
    const keys: string[] = [];

    for(let bucket of this.keyMap) {
      if(!bucket) continue;
      for(let item of bucket){
        keys.push(item[0]);
      }
    }
    return keys;
  }

  values() {
    const values= new Set<any>();

    for(let bucket of this.keyMap) {
      if(!bucket) continue;
      for(let item of bucket) {
        values.add(item[1]);
      }
    }
    return values;
  }
}

const ht = new HashTable(5);

ht.set("oranges", 5);
ht.set("apples", 3);
ht.set("eggs", 12);
ht.set("plums", 12);
ht.set("milk", 4);
ht.set("oranges", 10);

// console.log(ht.get("apples"));
// console.log(ht.get("bananas"));
// console.log(ht.keyMap);

console.log(ht.keys());
console.log(ht.values());
