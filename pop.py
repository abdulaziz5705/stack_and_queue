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


# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(5)
# print(f"Elements: {stack.data}")
# print(f"Pop element: {stack.pop()}")
# print(f"After pop Elements: {stack.data}")

#
# stack = Stack()
# stack.push("banana")
# stack.push("phone")
# stack.push("monitor")
# print(f"Elements: {stack.data}")
# print(f"Pop element: {stack.pop()}")
# print(f"After pop Elements: {stack.data}")

stack = Stack()
stack.push("number")
stack.push("kola")
stack.push("tiger")
if stack.is_empty():
    print("Stack is empty")

else:

    print(f"Elements: {stack.data}")
    print(f"Pop element: {stack.pop()}")
    print(f"After pop Elements: {stack.data}")
