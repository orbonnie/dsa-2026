class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def get_next_val(self):
        if not self.next: return None

        return self.next.value

    def get_prev_val(self):
        if not self.prev: return None

        return self.prev.value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, val):
        new_node = Node(val)

        if not self.length:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node

        self.tail = new_node
        self.length += 1

        return self

    def pop(self):
        old_tail = self.tail
        if not old_tail: return

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            old_tail.prev = None

        self.length -= 1

        return old_tail


    def shift(self):
        pass

    def unshift(self, val):
        pass

    def get(self, idx):
        pass

    def set(self, idx, val):
        pass

    def insert(self, idx, val):
        pass

    def remove(self, idx):
        pass

    def print(self):
        display = []

        curr = self.head
        while curr:
            node = {f"val: {curr.value}, prev: {curr.get_prev_val()}, next: {curr.get_next_val()}"}
            display.append(node)
            curr = curr.next

        print(display)

    def print_list(self):
        display = []

        curr = self.head
        while curr:
            display.append(curr.value)
            curr = curr.next

        print(display)

dll = DoublyLinkedList()
dll.push(7)
dll.push(9)
dll.push(11)
dll.push(12)
dll.print_list()
dll.print()

# print(dll.pop().value)
# print(dll.pop().value)
# dll.print_list()

# print(dll.pop().value)
# print(dll.pop().value)
# print(dll.pop())
# print(dll.pop())
# print(dll.pop())
# dll.print_list()