# coding:utf-8

""""
用数组实现队列
"""


class ArrayQueue:

    def __init__(self, capacity: int):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item: str) -> bool:
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:  # 队列中前面有空的位置,进行数据搬移
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                # 搬移完成后，修改头尾指针指向
                self._tail -= self._head
                self._head = 0
        self._items.insert(self._tail, item)
        self._tail += 1
        return True

    def dequeue(self) -> str:
        if self._tail != self._head:
            item = self._items[self._head]
            self._head += 1
            return item
        else:
            return None

    def __repr__(self) -> str:
        return " ".join(item for item in self._items[self._head:self._tail])


if __name__ == '__main__':
    array_queue = ArrayQueue(3)
    print(array_queue.enqueue('1'))
    print(array_queue.enqueue('2'))
    print(array_queue.enqueue('3'))
    print(array_queue.enqueue('4'))
    print(array_queue)
    print(array_queue.dequeue())
    print(array_queue)
    print(array_queue.dequeue())
    print(array_queue.dequeue())
    print(array_queue)
