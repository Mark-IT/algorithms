"""
基于数组的循环队列
"""
from itertools import chain


class CircularQueue:
    def __init__(self, capacity: int):
        self.items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def is_full(self):
        return (self._tail + 1) % self._capacity == self._head

    def is_empty(self):
        return self._tail == self._head

    def enqueue(self, item: str) -> bool:
        if self.is_full():
            return False
        self.items.append(item)
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self) -> str:
        if not self.is_empty():
            item = self.items[self._head]
            self._head = (self._head + 1) % self._capacity
            return item

    def __repr__(self):
        if self._tail >= self._head:
            return " ".join(self.items[self._head:self._tail])
        else:
            return " ".join(chain(self.items[self._head:], self.items[:self._tail]))


if __name__ == '__main__':

    queue = CircularQueue(5)

    for i in range(5):
        queue.enqueue(str(i))
    print(queue)

    for _ in range(3):
        print(queue.dequeue())

    queue.enqueue('a')
    queue.enqueue('b')
    for _ in range(3):
        queue.dequeue()
    print(queue)
