class BinaryHeap{
  values: number[]
  isMax: boolean

  constructor(isMax: boolean) {
    this.values = [];
    this.isMax = isMax;
  }

  size(): number {return this.values.length};
  peek(): number {return this.values[0]};

  compare(a:number, b:number) {
    return this.isMax ? a > b : a < b;
  }

  insert(val: number) {
    this.values.push(val);
    this.bubbleUp(this.values.length - 1);
  }

  pop() {
    const len = this.size();

    if(len === 0) return;
    if(len === 1) return this.values.pop();

    const head = this.values[0];
    [this.values[0], this.values[len - 1]] = [this.values[len - 1], this.values[0]];
    this.values.pop();
    this.sinkDown(0);

    return head;
  }

  bubbleUp(idx: number) {
    while(idx > 0) {
      let parent = Math.floor((idx - 1) / 2);
      if(this.compare(this.values[idx], this.values[parent])) {
        [this.values[idx], this.values[parent]] = [this.values[parent], this.values[idx]];
        idx = parent;
      } else break;
    }
  }

  sinkDown(idx: number) {
    const n = this.size();
    while(true) {
      let best = idx;
      let lChild = 2*idx + 1;
      let rChild = 2*idx + 2;


      if(lChild < n && this.compare(this.values[lChild], this.values[best])) best = lChild;
      if(rChild < n && this.compare(this.values[rChild], this.values[best])) best = rChild;
      if (best === idx) break;

      [this.values[idx], this.values[best]] = [this.values[best], this.values[idx]];
      idx = best;
    }
  }
}

const heap = new BinaryHeap(false);
// 41, 39, 33, 18, 27, 12
heap.insert(55);
heap.insert(28);
heap.insert(48);
heap.insert(14);
heap.insert(32);
heap.insert(29);

console.log(heap.values);

heap.pop();
console.log(heap.values);

heap.pop();
console.log(heap.values);

heap.pop();
console.log(heap.values);
