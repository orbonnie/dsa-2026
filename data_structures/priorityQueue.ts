class QueueNode {
  value: any
  priority: number

  constructor(value: any, priority: number) {
    this.value = value;
    this.priority = priority;
  }
}

class PriorityQueue {
  values: any[] = [];

  size() {return this.values.length - 1};
  peek() {return this.values[0]};

  enqueue(val: any, priority: number) {
    const node = new QueueNode(val, priority);
    this.values.push(node);
    this.bubbleUp(this.size());
  }

  bubbleUp(idx: number) {
    while(idx > 0) {
      const parent = Math.floor((idx - 1) / 2);
      if(this.values[idx].priority < this.values[parent].priority) {
        [this.values[idx], this.values[parent]] = [this.values[parent], this.values[idx]];
        idx = parent;
      } else break;
    }
  }

  dequeue() {
    const head = this.values[0];
    const end = this.size();
    if(this.size() === 0) return;
    if(this.size() === 1) return this.values.pop();

    [this.values[0], this.values[end]] = [this.values[end], this.values[0]];
    this.values.pop();

    this.sinkDown(0);

    return head;

  }

  sinkDown(idx: number) {
    const end = this.size();
    while(true) {
      let best = idx;
      const left = idx*2 + 1;
      const right = idx*2 + 2;

      if(left <= end && this.values[best].priority > this.values[left].priority) best = left;
      if(right <= end && this.values[best].priority > this.values[right].priority) best = right;
      if(idx === best) break;

      [this.values[best], this.values[idx]] = [this.values[idx], this.values[best]];
      idx = best;
    }
  }
}


const pq = new PriorityQueue();
pq.enqueue("bread", 2);
pq.enqueue("candy", 7);
pq.enqueue("milk", 1);
pq.enqueue("juice", 5);
pq.enqueue("yogurt", 3);
pq.enqueue("oranges", 1);
console.log(pq);

pq.dequeue();
console.log(pq);

pq.dequeue();
console.log(pq);
