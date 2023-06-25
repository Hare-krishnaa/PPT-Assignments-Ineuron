class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Queue is empty.")

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # 10
print(queue.dequeue())  # 20
print(queue.dequeue())  # 30

print(queue.is_empty())  # True
