class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty")

#
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
#
# print("Queue:", queue.items)
# print(f"Enqueue: {queue.dequeue()}")


queue = Queue()
queue.enqueue("apple")
queue.enqueue(2)
queue.enqueue("john")

print("Queue:", queue.items)
print(f"Enqueue: {queue.dequeue()}")