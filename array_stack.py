class ArrayStack:
    """A fixed-capacity stack implemented with a Python list as an array."""

    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Stack capacity must be greater than zero.")
        self._items = [None] * capacity
        self._top = -1
        self._capacity = capacity

    def push(self, item):
        if self.is_full():
            raise OverflowError("ArrayStack overflow: cannot push; the stack is full.")
        self._top += 1
        self._items[self._top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("ArrayStack underflow: cannot pop; the stack is empty.")
        item = self._items[self._top]
        self._items[self._top] = None
        self._top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("ArrayStack underflow: cannot peek; the stack is empty.")
        return self._items[self._top]

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._capacity - 1

    def __str__(self):
        return f"bottom -> top: {[x for x in self._items[:self._top + 1]]} (capacity={self._capacity})"
