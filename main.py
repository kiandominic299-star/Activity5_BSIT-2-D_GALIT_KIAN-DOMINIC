from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import CircularArrayQueue
from linked_queue import LinkedQueue
from applications import parentheses_balanced, run_print_queue


def show_state(structure):
    print("Current structure:", structure)


def operate_stack(stack):
    while True:
        print("\nStack operations: 1 Push  2 Pop  3 Peek  4 Is empty  5 Is full  0 Back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                stack.push(input("Value to push: "))
            elif choice == "2":
                print("Popped:", stack.pop())
            elif choice == "3":
                print("Top item:", stack.peek())
            elif choice == "4":
                print("Is empty:", stack.is_empty())
            elif choice == "5":
                print("Is full:", stack.is_full() if hasattr(stack, "is_full") else "No fixed capacity")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
                continue
            show_state(stack)
        except (IndexError, OverflowError, ValueError) as error:
            print("ERROR:", error)
            show_state(stack)


def operate_queue(queue):
    while True:
        print("\nQueue operations: 1 Enqueue  2 Dequeue  3 Peek front  4 Is empty  5 Is full  0 Back")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                queue.enqueue(input("Value to enqueue: "))
            elif choice == "2":
                print("Dequeued:", queue.dequeue())
            elif choice == "3":
                print("Front item:", queue.peek_front())
            elif choice == "4":
                print("Is empty:", queue.is_empty())
            elif choice == "5":
                print("Is full:", queue.is_full() if hasattr(queue, "is_full") else "No fixed capacity")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
                continue
            show_state(queue)
        except (IndexError, OverflowError, ValueError) as error:
            print("ERROR:", error)
            show_state(queue)


def get_capacity():
    while True:
        try:
            capacity = int(input("Enter array capacity (e.g. 5): "))
            if capacity > 0:
                return capacity
            print("Capacity must be greater than zero.")
        except ValueError:
            print("Enter a whole number.")


def main():
    while True:
        print("\n=== STACKS AND QUEUES LAB ===")
        print("1 ArrayStack")
        print("2 LinkedStack")
        print("3 Circular ArrayQueue")
        print("4 LinkedQueue")
        print("5 Check balanced parentheses")
        print("6 Simulate print queue")
        print("0 Exit")
        choice = input("Select implementation/application: ").strip()

        if choice == "1":
            operate_stack(ArrayStack(get_capacity()))
        elif choice == "2":
            operate_stack(LinkedStack())
        elif choice == "3":
            operate_queue(CircularArrayQueue(get_capacity()))
        elif choice == "4":
            operate_queue(LinkedQueue())
        elif choice == "5":
            expression = input("Enter an expression containing (), [] or {}: ")
            print("Balanced." if parentheses_balanced(expression) else "Not balanced.")
        elif choice == "6":
            run_print_queue()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
