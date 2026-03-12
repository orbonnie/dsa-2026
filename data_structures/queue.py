class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enque(self, val):
        node = Node(val)

        if not self.first:
            self.first = node
        else:
            self.last.next = node

        self.last = node
        self.size += 1

        return self.size



    def deque(self):
        if not self.size: return None

        node = self.first

        if self.size == 1:
            self.last = None

        self.first = node.next
        self.size -= 1

        return node.value

    def __repr__(self):
        items = []
        curr = self.first

        while curr:
            items.append(str(curr.value))
            curr = curr.next

        return f"[{'->'.join(items)}]"


q = Queue()
q.enque(4)
q.enque(6)
q.enque(7)
q.enque(9)
q.enque(12)
print(q)
print("first", q.first.value)
print("first.next", q.first.next.value)
print("last", q.last.value)

q.deque()
q.deque()
q.deque()
print(q)
print("first", q.first.value)
print("first.next", q.first.next.value)
print("last", q.last.value)
