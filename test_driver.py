"""Simple test driver for all four data structures and lab applications."""
from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import CircularArrayQueue
from linked_queue import LinkedQueue
from applications import parentheses_balanced


def test_stack(stack):
    print("\nTesting", type(stack).__name__)
    stack.push("A")
    stack.push("B")
    print("After pushes:", stack)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("After pop:", stack)


def test_queue(queue):
    print("\nTesting", type(queue).__name__)
    for value in ("A", "B", "C"):
        queue.enqueue(value)
    print("After enqueues:", queue)
    print("Peek front:", queue.peek_front())
    print("Dequeue:", queue.dequeue())
    print("After dequeue:", queue)


def main():
    test_stack(ArrayStack(3))
    test_stack(LinkedStack())
    test_queue(CircularArrayQueue(3))
    test_queue(LinkedQueue())

    print("\nCIRCULAR QUEUE WRAP-AROUND DEMONSTRATION")
    queue = CircularArrayQueue(4)
    for value in ("A", "B", "C", "D"):
        queue.enqueue(value)
    print("Filled:", queue)
    print("Removed:", queue.dequeue())
    print("Removed:", queue.dequeue())
    queue.enqueue("E")
    queue.enqueue("F")  # rear wraps to the beginning of the array
    print("After adding E and F (wrap-around):", queue)

    print("\nERROR HANDLING DEMONSTRATION")
    small_stack = ArrayStack(1)
    small_stack.push("Only item")
    try:
        small_stack.push("Extra item")
    except OverflowError as error:
        print("Expected overflow:", error)
    try:
        small_stack.pop()
        small_stack.pop()
    except IndexError as error:
        print("Expected underflow:", error)

    small_queue = CircularArrayQueue(1)
    small_queue.enqueue("Only job")
    try:
        small_queue.enqueue("Extra job")
    except OverflowError as error:
        print("Expected queue overflow:", error)
    try:
        small_queue.dequeue()
        small_queue.dequeue()
    except IndexError as error:
        print("Expected queue underflow:", error)

    print("\nPARENTHESIS CHECKER")
    for sample in ("{[()]}", "([)]", "((())", "a+(b*c)"):
        print(sample, "=>", "Balanced" if parentheses_balanced(sample) else "Not balanced")


if __name__ == "__main__":
    main()
