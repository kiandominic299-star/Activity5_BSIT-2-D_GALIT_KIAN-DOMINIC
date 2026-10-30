OPENING = {"(": ")", "[": "]", "{": "}"}


def parentheses_balanced(expression):
    """Return True when (), [] and {} are correctly balanced and nested."""
    stack = []
    for character in expression:
        if character in OPENING:
            stack.append(character)
        elif character in ")]}":
            if not stack or OPENING[stack.pop()] != character:
                return False
    return not stack


def run_print_queue():
    """Demonstrate FIFO print jobs using a queue."""
    from linked_queue import LinkedQueue

    queue = LinkedQueue()
    print("\nPRINT QUEUE: enter jobs; blank ID ends input.")
    while True:
        job_id = input("Job ID: ").strip()
        if not job_id:
            break
        try:
            pages = int(input("Number of pages: "))
            if pages <= 0:
                print("Page count must be positive.")
                continue
        except ValueError:
            print("Please enter a whole number for pages.")
            continue
        queue.enqueue({"id": job_id, "pages": pages})
        print("Queued:", job_id, "| pages:", pages)
        print("Queue state:", queue)

    print("\nPrinting in FIFO (first-in, first-out) order:")
    position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"Wait position {position}: Job {job['id']} ({job['pages']} pages)")
        position += 1
    print("All print jobs completed.")
