# -*- coding: utf-8 -*-


class LRUNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    '''
    leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
            当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    '''

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # self.top和self.tail作为哨兵节点, 避免越界
        self.top = LRUNode(None, -1)
        self.tail = LRUNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def insert_head(self, node):
        top_node = self.top.next
        self.top.next = node
        node.prev = self.top
        node.next = top_node
        top_node.prev = node

    def get(self, key: int) -> int:

        if key in self.cache.keys():
            # 更新结点顺序
            cur = self.cache[key]
            # 跳出原位置
            cur.next.prev = cur.prev
            cur.prev.next = cur.next
            # 最近用过的置于链表首部
            self.insert_head(cur)

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.keys():
            cur = self.cache[key]
            cur.val = value
            # 跳出原位置
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # 最近用过的置于链表首部
            self.insert_head(cur)
        else:
            # 增加新结点至首部
            cur = LRUNode(key, value)
            self.cache[key] = cur
            # 最近用过的置于链表首部
            self.insert_head(cur)
            if len(self.cache.keys()) > self.cap:
                self.cache.pop(self.tail.prev.key)
                # 去掉原尾结点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)
    cache.get(1)  # 返回  1
    cache.put(3, 3)  # 该操作会使得密钥 2 作废
    print(cache)
    cache.get(2)  # 返回 -1 (未找到)
    cache.put(4, 4)  # 该操作会使得密钥 1 作废
    print(cache)
    cache.get(1)  # 返回 -1 (未找到)
    cache.get(3)  # 返回  3
    print(cache)
    cache.get(4)  # 返回  4
    print(cache)
