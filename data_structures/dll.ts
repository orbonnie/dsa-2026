export {};

class ListNode {
  value: any
  next: (ListNode | null)
  prev: (ListNode | null)

  constructor(value: any) {
    this.value = value;
    this.next = null;
    this.prev = null;
  };
};


class DoublyLinkedList {
  head: (ListNode | null) = null
  tail: (ListNode | null) = null
  length: number = 0

  push(val: any) {
    const node = new ListNode(val);

    if (!this.head) {
      this.head = node;
    } else {
      this.tail!.next = node;
      node.prev = this.tail;
    }
    this.tail = node;
    this.length++;

    return this;
  }

  pop() {
    const popped = this.tail;
    if (!popped) return;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = this.tail!.prev;
      this.tail!.next = null;
      popped!.prev = null;
    }

    this.length--;

    return popped;
  }

  shift() {
    const shifted = this.head;
    if (!shifted) return;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head!.next;
      this.head!.prev = null;
      shifted.next = null;
    }

    this.length--;

    return shifted;
  }

  unshift(val: any) {
    const node = new ListNode(val);

    if (!this.head) {
      this.tail = node;
    } else {
      this.head.prev = node;
      node.next = this.head;
    }

    this.head = node;
    this.length++;

    return this;
  }

  get(idx: number) {
    if(idx < 0 || idx >= this.length) return;

    let curr: ListNode;

    if ((this.length - idx) > idx ) {
      curr = this.head!;
      for (let i = 0; i < idx; i++) {
        curr = curr!.next!;
      }
    } else {
      curr = this.tail!;
      for (let i = this.length - 1; i > idx; i--) {
        curr = curr!.prev!;
      }
    }

    return curr;
  }

  set(idx:number, val: any) {
    const node = this.get(idx);

    if (!node) return false;

    node.value = val;

    return true;
  }

  insert(idx: number, val: any) {
    const node = new ListNode(val);
    const prevNode = this.get(idx - 1);

    if (idx === 0) this.unshift(val);
    else if (idx === this.length) this.push(val);
    else if (!prevNode) return false;
    else {
      const nextNode = prevNode!.next;
      node.next = nextNode;
      node.prev = prevNode!;
      nextNode!.prev = node;
      prevNode!.next = node;
      this.length++;
    }

    return true;
  }

  remove(idx: number) {
    const currNode = this.get(idx);

    if (idx === 0) return this.shift();
    if (idx === this.length - 1) return this.pop();
    if (!currNode || idx >= this.length) return;

    const prevNode = currNode.prev;
    const nextNode = currNode.next;
    prevNode!.next = nextNode;
    nextNode!.prev = prevNode;

    currNode.prev = null;
    currNode.next = null;

    this.length--;
    return currNode;
  }

  print() {
    let arr = [];
    let curr = this.head;
    while(curr) {
      arr.push(curr.value);
      curr = curr.next;
    }
    console.log(arr);
  }
}

const list = new DoublyLinkedList();
list.push(3);
list.push(10);
list.push(8);
list.unshift(5);
list.unshift(6);
list.unshift(7);
// list.set(5, 4);
// list.insert(0, 4);
// list.insert(6, 4);
// list.insert(7, 4);
// list.insert(-2, 4);
list.print();
list.remove(4);
list.print();
console.log(list.get(3));
console.log(list.get(4));
// list.remove(0);
// list.remove(2);
list.remove(7);
list.remove(-7);
// console.log(list.get(2));
