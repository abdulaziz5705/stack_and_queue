

class Stack:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        return self.data == 0

    def push(self, item):
        self.data.append(item)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.data)
print(stack.isEmpty())

