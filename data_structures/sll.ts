class ListNode {
  value: number
  next: (ListNode | null)

  constructor(value: any) {
    this.value = value;
    this.next = null;
  }
}

class SinglyLinkedList {
  head: (ListNode | null) = null;
  tail: (ListNode | null) = null;
  length: number = 0;

  push(val: any) {
    const node = new ListNode(val);

    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail!.next = node;
      this.tail = node;
    }

    this.length++;

    return this;
  }

  pop() {
    let curr = this.head;
    if (!curr) return;


    if (curr === this.tail) {
      const poppedNode = this.head;
      this.head = null;
      this.tail = null;
      this.length--;

      return poppedNode;
    }

    while(curr!.next !== this.tail) {
      curr = curr!.next;
    }

    const poppedNode = curr!.next;
    this.tail = curr;
    this.tail!.next = null;
    this.length--;

    return poppedNode;
  }

  shift() {
    const curr = this.head;

    if(!curr) return;

    const popped = curr;

    if(curr === this.tail) {
      this.head = null;
      this.tail = null;
      this.length--;

      return popped;
    }

    this.head = curr.next;
    this.length--;

    return popped;
  }

  unshift(val: any) {
    const node = new ListNode(val);
    const curr = this.head;

    if(!curr) {
      this.tail = node;
    } else {
      node.next = curr;
    }

    this.head = node;
    this.length++;

    return this;
  }

  get(idx: number) {
    if(idx < 0|| idx >= this.length) return;

    let curr = this.head;

    for (let i = 0; i < idx; i++) {
      curr = curr!.next;
    }

    return curr;
  }

  set(idx: number, val: any) {
    const node = this.get(idx);

    if(!node) return false;

    node!.value = val;

    return true;
  }

  insert(idx: number, val: any) {
    const prevNode = this.get(idx - 1);

    if (idx === 0) this.unshift(val);
    else if (idx === this.length) this.push(val);
    else if (!prevNode) return false;

    else {
      const newNode = new ListNode(val);
      newNode.next = prevNode.next;
      prevNode.next = newNode;
      this.length++;
    }

    return true;
  }

  remove(idx: number) {
    const prevNode = this.get(idx - 1);

    if (idx === 0) return this.shift();
    else if (idx === this.length - 1) return this.pop();
    else if (!prevNode || idx === this.length) return;
    else {
      const currNode = prevNode.next;
      prevNode.next = currNode!.next;
      this.length--;

      return currNode;
    }
  }

  reverse() {
    if (this.length < 2) return this;
    const prevHead = this.head;
    let next: (ListNode | null);
    let prev: (ListNode | null) = null;
    let curr = this.head;

    while (curr) {
      next = curr!.next;
      curr!.next  = prev;
      prev = curr;
      curr = next;
    }

    this.head = prev;
    this.tail = prevHead;

    this.print();

    return this;
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


const list = new SinglyLinkedList();
list.push(3);
list.push(10);
list.push(8);
list.unshift(5);
list.unshift(6);
list.unshift(7);
// 7, 6, 5, 3, 10, 8
list.insert(3, 4);
// console.log(list.get(2));
// console.log(list.get(3));
// console.log(list.get(4));
console.log(list.insert(7, 50));
console.log(list.get(7));
console.log(list.insert(0, 0));
console.log(list.insert(10, 100));
// 0, 7, 6, 5, 4, 3, 10, 8, 50
// console.log(list.remove(0));
// console.log(list.remove(8));
// console.log(list.remove(7));
// 7, 6, 5, 4, 3, 10, 8
// console.log(list.remove(3));
// 7, 6, 5, 3, 10, 8
// console.log(list.get(3));
// console.log(list.insert(-10, 100));
console.log(list);
console.log(list.reverse());
// 0, 7, 6, 5, 4, 3, 10, 8, 50
// console.log(list.get(2));
// console.log(list.set(2, 11));
// console.log(list.set(-8, 11));
// console.log(list.get(2));
// console.log(list.get(6));
// console.log(list.get(-2));
// console.log(list.shift());
// console.log(list.shift());
// console.log(list.shift());
// console.log(list.shift());
// console.log(list.pop());
// console.log(list.pop());
// console.log(list.pop());
// console.log(list.pop());
