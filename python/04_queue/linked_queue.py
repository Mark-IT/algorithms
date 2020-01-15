"""
基于链表的队列
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedQueue:
    def __init__(self):
        self._head: Node = None
        self._tail: Node = None

    def enqueue(self, value: str):
        new_node = Node(value)
        if self._tail:
            self._tail.next_node = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> str:
        if self._head:
            data = self._head.data
            self._head = self._head.next_node
            if not self._head:
                self._tail = Node
            return data

    def __repr__(self):
        values = []
        cur = self._head
        while cur:
            values.append(cur.data)
            cur = cur.next_node
        return "->".join(values)


if __name__ == '__main__':

    queue = LinkedQueue()

    for i in range(10):
        queue.enqueue(str(i))
    print(queue)

    for _ in range(5):
        print(queue.dequeue())

    queue.enqueue('a')
    queue.enqueue('b')
    print(queue)
