class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # 30
print(stack.pop())  # 20
print(stack.pop())  # 10

print(stack.is_empty())  # True
