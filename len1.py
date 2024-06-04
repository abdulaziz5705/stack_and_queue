class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)


stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
print(stack.is_empty())
print(stack.data)
