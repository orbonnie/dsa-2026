class StackNode {
  value: any
  next: (StackNode | null)

  constructor(value: any) {
    this.value = value
    this.next = null
  }
}

class Stack {
  first: (StackNode | null);
  last: (StackNode | null);
  size: number;

  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(val: any) {
    const new_node = new StackNode(val)

    if(!this.last) {
      this.last = new_node;
    } else {
      new_node.next = this.first;
    }

    this.first = new_node;
    this.size++;

    return this.size;
  }

  pop() {
    if(!this.first) return;

    const old_head = this.first;

    if(this.size === 1) {
      this.first = null;
      this.last = null;
    } else {
      this.first = this.first.next;
    }

    this.size--;

    return old_head.value;
  }

  print() {
    const items = [];
    let curr = this.first;

    while(curr) {
      items.push(curr.value);
      curr = curr.next;
    }

    console.log(items)
  }
}

const stack = new Stack();

console.log(stack.push(3));
console.log(stack.push(2));
console.log(stack.push(5));
console.log(stack.push(7));

console.log(stack);

console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());

console.log(stack);
