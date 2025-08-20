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
