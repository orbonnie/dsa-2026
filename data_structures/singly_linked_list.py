class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Singly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

        return self





first = Node(5)
first.next = Node(3)
first.next.next = Node(10)

for att, v in vars(first).items():
    print(f"{att:>12} : {v}")