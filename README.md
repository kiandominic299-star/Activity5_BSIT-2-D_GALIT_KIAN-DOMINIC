# Stacks and Queues: Array vs. Linked List

## Description
This Python laboratory program implements four data structures from first principles:

- `ArrayStack`: fixed-capacity stack using an array.
- `LinkedStack`: stack using linked nodes, with no fixed capacity.
- `CircularArrayQueue`: fixed-capacity FIFO queue using circular indexing and a size counter.
- `LinkedQueue`: FIFO queue using linked nodes with head and tail references.

The menu-driven program allows the user to choose an implementation and perform its operations. The state is displayed after each successful operation and after errors. The applications include a balanced-parentheses checker and a FIFO print-queue simulation.

## Files
| File | Description |
|---|---|
| `array_stack.py` | Array-based stack class |
| `linked_stack.py` | Linked-list stack class |
| `array_queue.py` | Circular array queue class |
| `linked_queue.py` | Linked-list queue class |
| `applications.py` | Parentheses checker and print-queue exercise |
| `main.py` | Interactive menu-driven program |
| `test_driver.py` | Demonstrations, wrap-around, and error tests |
| `analysis.md` | Written response to the analysis question |

## Requirements
- Python 3.8 or later
- No external libraries required

## How to Run
1. Download or clone the repository.
2. Open a terminal in the folder containing the files.
3. Run the interactive menu:

   ```bash
   python main.py
   ```

4. To run the demonstrations and tests:

   ```bash
   python test_driver.py
   ```

Run either command from the same folder so Python can find the four class files.

## Operations
**ArrayStack:** `push`, `pop`, `peek`, `is_empty`, `is_full`.

**LinkedStack:** `push`, `pop`, `peek`, `is_empty`.

**CircularArrayQueue:** `enqueue`, `dequeue`, `peek_front`, `is_empty`, `is_full`.

**LinkedQueue:** `enqueue`, `dequeue`, `peek_front`, `is_empty`.

Array implementations ask for a positive capacity. Linked implementations grow as nodes are added, subject to available memory. Empty removals/peeks raise `IndexError`; attempts to add to a full array structure raise `OverflowError`.

## Sample Run: Error Handling
A sample of the expected messages:

```text
Expected overflow: ArrayStack overflow: cannot push; the stack is full.
Expected underflow: ArrayStack underflow: cannot pop; the stack is empty.
Expected queue overflow: CircularArrayQueue overflow: cannot enqueue; the queue is full.
Expected queue underflow: CircularArrayQueue underflow: cannot dequeue; the queue is empty.
```

## Circular Queue Wrap-Around
The test driver fills a queue, removes two items, then enqueues two more. The rear index wraps to the beginning of the underlying array. Run `python test_driver.py` to see the state and indexes.

## GitHub Submission Checklist
1. Create/sign in to your GitHub account for the course.
2. Create a repository using the required naming pattern: `Activity#_Section_LASTNAME_FIRSTNAME` (replace the placeholders with the exact activity number, section, surname, and first name required by your instructor).
3. Upload each `.py`, `.md` file individually. Do not upload an archive file.
4. Check that `README.md` and `analysis.md` are visible in the repository.
5. Copy the repository URL and submit it to the LMS before the deadline.
