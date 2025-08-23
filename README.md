# Python Queue Implementation

This project provides a full **Queue (FIFO)** data structure implementation in Python.  
It supports operations like `enqueue`, `dequeue`, `peek`, `clear`, `to_list`, and more.  

---

## Project Structure

queue_project/

|

├── my_queue.py

├── main.py

├── README.md


---

## Features

- **Enqueue**: Add a new element to the end of the queue.  
- **Dequeue**: Remove and return the first element of the queue.  
- **Peek**: Get the first element without removing it.  
- **Clear**: Empty the queue.  
- **Indexing**: Access and modify elements by index (`q[0]`, `q[-1]`).  
- **Iteration**: Iterate through the queue using a for-loop.  
- **Conversion**: Convert the queue to a list with `to_list()`.  

---

## Usage Example

```python
from my_queue import Queue, QueueIsEmpty

# Initialize queue
q = Queue()

# Enqueue elements
for i in range(5):
    q.enqueue(i)
print("Queue:", q)  # Output: 0->1->2->3->4

# Dequeue elements
try:
    while True:
        value = q.dequeue()
        print(f"Dequeued: {value}, Queue: {q}")
except QueueIsEmpty:
    print("Queue is empty now.")

# Peek
q.enqueue(100)
print("Peek:", q.peek())  # Output: 100

# Indexing
q[0] = 111
print("Updated Queue:", q)

# Iteration
for item in q:
    print(item)

# Convert to list
print("List view:", q.to_list())

# Clear queue
q.clear()
print("Cleared Queue:", q)
```
## Notes

The queue raises a QueueIsEmpty exception when trying to dequeue or peek from an empty queue.

This implementation uses a linked-list under the hood for efficient enqueue and dequeue operations.
