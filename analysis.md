# Analysis: Stacks and Queues

A linked-list stack pushes and pops at the **head** because both operations take **O(1)** time: the program only changes the head reference. Pushing or popping at the tail of a singly linked list would require traversing the list to find the node before the tail, which takes **O(n)** time. An array queue must be circular so that positions freed by dequeue operations can be reused when the rear reaches the physical end of the array. Circular indexing moves an index back to zero using modulo arithmetic, avoiding wasted spaces and unnecessary shifting of elements.
