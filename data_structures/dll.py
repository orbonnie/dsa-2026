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
        old_head = self.head
        if not self.length: return

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            old_head.next = None

        self.length -= 1

        return old_head


    def unshift(self, val):
        new_node = Node(val)

        if not self.length:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node
        self.length += 1

        return self


    def get(self, idx):
        if idx >= self.length or idx < 0: return

        curr = None

        if (self.length - idx) > idx:
            curr = self.head
            for i in range(idx):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.length -1, idx, -1):
                curr = curr.prev

        return curr


    def set(self, idx, val):
        node = self.get(idx)

        if not node: return False

        node.value = val

        return True


    def insert(self, idx, val):
        new_node = Node(val)
        prev_node = self.get(idx - 1)

        if idx == 0: self.unshift(val)
        elif idx == self.length: self.push(val)
        elif not prev_node: return False
        else:
            next_node = prev_node.next

            new_node.next = next_node
            new_node.prev = prev_node
            prev_node.next = new_node
            next_node.prev = new_node

            self.length += 1

        return True


    def remove(self, idx):
        curr_node = self.get(idx)

        if idx == 0: return self.shift()
        if idx == self.length - 1: return self.pop()
        if not curr_node: return

        prev_node = curr_node.prev
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node

        curr_node.prev = None
        curr_node.next = None

        self.length -= 1

        return curr_node


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
dll.push(13)
dll.push(14)
dll.push(15)
dll.print_list()
# dll.print()
# 7 9 11 12
print(dll.get(2).value)
dll.set(5, 20)
dll.print_list()
dll.remove(4)
dll.insert(2, 10)
dll.print_list()

print(dll.insert(12, 10))
print(dll.insert(-2, 10))
print(dll.set(-2, 10))
print(dll.set(12, 10))
print(dll.get(-3))
print(dll.get(13))
print(dll.remove(14))
print(dll.remove(-4))
# print(dll.pop().value)
# print(dll.pop().value)
# dll.print_list()

# print(dll.pop().value)
# print(dll.pop().value)
# print(dll.pop())
# print(dll.pop())
# print(dll.pop())
# dll.print_list()