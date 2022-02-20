class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self,item):
        self.stack.append(item)

    def __len__(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
