# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedStack:

    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value=value)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.top:
            value = self.top.value
            self.top = self.top.next_node
            return value

    def is_empty(self):
        return self.top is None

    def __repr__(self):
        cur = self.top
        values = ""
        while cur:
            values += str(cur.value)
            cur = cur.next_node
            if cur:
                values += '->'
        return values


if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)
