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


# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push("ali")
# stack.push("doctor")
# if stack.size() == 4:
#     print(stack.peek())
#
# else:
#     print(stack.data)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push("ali")
stack.push("doctor")
print(f"Elements: {stack.data}")
#print(f"Pop element: {stack.pop()}")
print(f"Peek element: {stack.peek()}")
print(f"Elements: {stack.data}")
