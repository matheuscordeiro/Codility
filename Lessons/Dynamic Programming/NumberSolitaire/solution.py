MIN_VALUE = -10001

class LinkedList:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def reverse(self):
        current = self
        before = None
        while current.next:
            node_next = current.next
            current.next = before
            before = current
            current = node_next

        current.next = before
        return current

if __name__ == "__main__":
    a = LinkedList(1)
    b = LinkedList(2)
    c = LinkedList(3)
    a.next = b
    b.next = c
    print(f"{a.value}->{a.next.value}->{a.next.next.value}")
    o = a.reverse()
    print(f"{c.value}->{c.next.value}->{c.next.next.value}")
