class _Node:
    """One node in a singly linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedStack:
    """A stack implemented by inserting and removing at the head."""

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, item):
        self._head = _Node(item, self._head)
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("LinkedStack underflow: cannot pop; the stack is empty.")
        item = self._head.data
        self._head = self._head.next
        self._size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("LinkedStack underflow: cannot peek; the stack is empty.")
        return self._head.data

    def is_empty(self):
        return self._head is None

    def __str__(self):
        values, current = [], self._head
        while current is not None:
            values.append(current.data)
            current = current.next
        return f"top -> bottom: {values} (size={self._size})"
