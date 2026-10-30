class _Node:
    """One node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    """A FIFO queue with head (front) and tail (rear) references."""

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        new_node = _Node(item)
        if self.is_empty():
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("LinkedQueue underflow: cannot dequeue; the queue is empty.")
        item = self._head.data
        self._head = self._head.next
        self._size -= 1
        if self._head is None:
            self._tail = None
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("LinkedQueue underflow: cannot peek; the queue is empty.")
        return self._head.data

    def is_empty(self):
        return self._head is None

    def __str__(self):
        values, current = [], self._head
        while current is not None:
            values.append(current.data)
            current = current.next
        return f"front -> rear: {values} (size={self._size})"
