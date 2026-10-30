class CircularArrayQueue:
    """A fixed-capacity FIFO queue using circular indexing and a size counter."""

    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Queue capacity must be greater than zero.")
        self._items = [None] * capacity
        self._capacity = capacity
        self._front = 0
        self._rear = 0
        self._size = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("CircularArrayQueue overflow: cannot enqueue; the queue is full.")
        self._items[self._rear] = item
        self._rear = (self._rear + 1) % self._capacity
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("CircularArrayQueue underflow: cannot dequeue; the queue is empty.")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return item

    def peek_front(self):
        if self.is_empty():
            raise IndexError("CircularArrayQueue underflow: cannot peek; the queue is empty.")
        return self._items[self._front]

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def __str__(self):
        values = [self._items[(self._front + i) % self._capacity]
                  for i in range(self._size)]
        return (f"front -> rear: {values} "
                f"(front_index={self._front}, rear_index={self._rear}, "
                f"size={self._size}/{self._capacity})")
