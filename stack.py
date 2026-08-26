class stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

stack_instance = stack()
stack_instance.push(1)
stack_instance.push(2)
print(stack_instance.pop())  # Output: 2
print(stack_instance.peek())  # Output: 1
print(stack_instance.size())  # Output: 1