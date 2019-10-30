# -*- coding: utf-8 -*-
import sys

# 引用当前文件夹下的single_linked_list
sys.path.append('singly_linked_list')
from single_linked_list import SingleLinkedList


def is_palindrome(l: SingleLinkedList) -> bool:
    head = l.head_node
    fast = l.head_node
    slow = l.head_node

    if head is None or  head.next_node is None:  # 空或1个节点
        return True

    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node

    # 当链表长度为奇数时，slow为中点，偶数时，slow为下中位

    # 将后半段翻转
    pre = None
    cur = slow
    next_node = cur.next_node
    while next_node:
        cur.next_node = pre
        pre = cur
        cur = next_node
        next_node = cur.next_node

    # 当前cur是最后一个节点，需要和它前面的节点进行最后一次倒置，来完成整个后半段倒置
    cur.next_node = pre

    # 3. cur就是倒置完成后的后半段的头节点,同时遍历cur和head，如果遍历完cur未出现不同的节点，则为回文链表

    while cur.next_node:
        if cur.data != head.data:
            return False
        cur = cur.next_node
        head = head.next_node
    # 此时cur为后半段的最后一个节点，还需要判断此时的cur和head的值是否相同
    return cur.data == head.data


if __name__ == '__main__':
    l = SingleLinkedList()
    assert is_palindrome(l) is True

    l1 = SingleLinkedList()
    for i in 'a':
        l1.insert_to_head(i)
    assert is_palindrome(l1) is True

    l2 = SingleLinkedList()
    for i in 'ab':
        l2.insert_to_head(i)
    assert is_palindrome(l2) is False

    l3 = SingleLinkedList()
    for i in 'aa':
        l3.insert_to_head(i)
    assert is_palindrome(l3) is True

    l4 = SingleLinkedList()
    for i in 'aba':
        l4.insert_to_head(i)
    assert is_palindrome(l4) is True

    l5 = SingleLinkedList()
    for i in 'abba':
        l5.insert_to_head(i)
    assert is_palindrome(l5) is True

    l6 = SingleLinkedList()
    for i in 'abcba':
        l6.insert_to_head(i)
    assert is_palindrome(l6) is True
