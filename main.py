from my_queue import Queue, QueueIsEmpty

def main():
    q = Queue()
    
    # 1. Enqueue qilish
    print("Enqueue qilish:")
    for i in range(5):
        q.enqueue(i)
        print(q)
    
    # 2. Dequeue qilish
    print("\nDequeue qilish:")
    try:
        while True:
            val = q.dequeue()
            print(f"Dequeued: {val}, Queue: {q}")
    except QueueIsEmpty as e:
        print(e)
    
    # 3. Peek
    q.enqueue(100)
    q.enqueue(200)
    print("\nPeek:", q.peek())
    
    # 4. Index orqali olish va o‘zgartirish
    print("\nIndex bilan ishlash:")
    print("Queue:", q)
    print("q[0] =", q[0])
    q[0] = 111
    print("Yangilangan Queue:", q)
    
    # 5. Iteratsiya
    print("\nIteratsiya qilish:")
    for item in q:
        print(item)
    
    # 6. List ko‘rinishi
    print("\nList view:", q.to_list())
    
    # 7. Clear
    q.clear()
    print("\nClear qilingan Queue:", q)

if __name__ == "__main__":
    main()
