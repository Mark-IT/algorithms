# -*- coding: utf-8 -*-

class ArrayStack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.stack.pop()

    @property
    def top(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        return self.size == 0

    def __repr__(self):
        return str(self.stack)


if __name__ == "__main__":
    stack = ArrayStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
