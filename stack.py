class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            print("Stack is empty")

    def size(self):
        if not self.is_empty():
            return len(self.data)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
top = stack.pop()
print(top)
print(stack.data)
