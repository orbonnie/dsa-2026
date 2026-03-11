class Node:
    def __init__(self, val):
      self.value = val
      self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if not self.first:
            self.first = node
            self.last = node
        else:
            node.next = self.first
            self.first = node

        self.size += 1

        return self.size

    def pop(self):
        if not self.first: return None

        node = self.first

        if self.size == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

        node.next = None
        self.size -= 1

        return node.value


    def __repr__(self):
        items = []
        current = self.first
        while current:
            items.append(str(current.value))
            current = current.next
        return f"Stack (top → bottom): [{' -> '.join(items)}]"

stack = Stack()

print(stack.push(3))
print(stack.push(2))
print(stack.push(5))
print(stack.push(7))

print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
