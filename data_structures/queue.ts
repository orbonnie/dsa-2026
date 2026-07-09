export {};

class QueueNode {
  value: any;
  next: (QueueNode | null);

  constructor(val: any) {
    this.value = val;
    this.next = null;
  }

}

  class Queue {
    first: (QueueNode | null);
    last: (QueueNode | null);
    size: number;

    constructor() {
      this.first = null;
      this.last = null;
      this.size = 0;
    }

    enqueue(val: any) {

    }

    dequeue() {

    }
  }
