class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_next_val(self):
        if not self.next:
            return None
        else: return self.next.val


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


    def pop(self):
        old_tail = self.tail
        if not old_tail: return

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            new_tail = self.head
            while new_tail.next != self.tail:
                new_tail = new_tail.next

            self.tail = new_tail
            self.tail.next = None

        self.length -= 1
        return old_tail


    def shift(self):
        old_head = self.head

        if not old_head: return

        if old_head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            old_head.next = None
            self.length -= 1

        return old_head


    def unshift(self, val):
        new_head = Node(val)

        if not self.length:
            self.tail = new_head
        else:
            new_head.next = self.head

        self.head = new_head
        self.length += 1

        return self


    def get(self, idx):
        if idx >= self.length or idx < 0: return

        curr = self.head

        for i in range(idx):
            curr = curr.next

        return curr


    def set(self, idx, val):
        node = self.get(idx)

        if node:
            node.val = val
            return True
        else: return False


    def insert(self, idx, val):
        prev_node = self.get(idx - 1)

        if idx == 0: self.unshift(val)
        elif idx == self.length: self.push(val)
        elif not prev_node: return False
        else:
            new_node = Node(val)
            new_node.next = prev_node.next
            prev_node.next = new_node
            self.length += 1

        return True


    def remove(self, idx):
        prev_node = self.get(idx - 1)

        if idx == 0: return self.shift()
        if idx == self.length -1: return self.pop()
        if not prev_node: return

        old_node = prev_node.next
        prev_node.next = old_node.next

        old_node.next = None
        self.length -= 1

        return old_node


    def reverse():
        pass

    def print(self):
        display = []
        curr = self.head

        while curr:
            display.append({
                "val": curr.val,
                "next": curr.get_next_val()
            })
            curr = curr.next

        print(display)






sll = Singly_Linked_List()
sll.push(5)
sll.push(10)
sll.push(15)
sll.push(20)
sll.print()
# p1 = sll.pop()
# p2 = sll.pop()

# print(f"val: {p1.val}, next: {p1.get_next_val()}")
# print(f"val: {p2.val}, next: {p2.get_next_val()}")

sll.unshift(11)
sll.unshift(12)
sll.unshift(13)
sll.unshift(14)
sll.print()

# print(sll.get(0).val)
# print(sll.get(3).val)
# print(sll.get(7).val)
# print(sll.get(8))
# print(sll.get(-8))

# print(sll.set(10, 100))
# print(sll.set(2, 16))
# print(sll.set(5, 88))
# print(sll.set(-2, 33))

sll.print()

print(sll.insert(10, 100))
print(sll.insert(3, 17))
print(sll.insert(9, 50))
print(sll.insert(0, 18))
print(sll.insert(-2, 180))

# p1 = sll.shift()
# p2 = sll.shift()
# print(f"val: {p1.val}, next: {p1.get_next_val()}")
# print(f"val: {p2.val}, next: {p2.get_next_val()}")
sll.print()

print(sll.remove(4).val)
print(sll.remove(0).val)
print(sll.remove(7).val)
print(sll.remove(13))
print(sll.remove(-4))
sll.print()

# for att, v in vars(first).items():
#     print(f"{att:>12} : {v}")