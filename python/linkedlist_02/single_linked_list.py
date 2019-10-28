# -*- coding: utf-8 -*-


class Node:
    def __init__(self, value, next_node=None):
        self.data = value
        self.next_node = next_node


class SingleLinkedList:

    def __init__(self):
        '''
        链表初始化
        '''
        self._head = None

    def insert_to_head(self, value: int):
        '''
        在链表头部插入一个值为data的节点
        :param value:
        :return:
        '''
        new_node = Node(value=value)
        new_node.next_node = self._head
        self._head = new_node

    def insert_node_after(self, node, value: int):

        '''
        在指定节点后插入新节点
        :param node:
        :param value:
        :return:
        '''

        if node is None:  # 如果指定在一个空节点之后插入数据节点，则什么都不做
            return

        new_node = Node(value)
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_node_before(self, node: Node, value: int):
        '''
        在指定节点前插入新节点
        :param node: 指定的节点 （假设其一定存在）
        :param value: 新节点的值
        :return:
        '''

        # if self._head is None:  # 空链表
        #     if node is None:  # 指定节点也为空，可认为是在头结点前插入
        #         self.insert_to_head(value)
        #     # 如果指定节点不为空，但是链表为空，则不处理，直接跳出
        #     return
        #     # 需要找到node的上一个节点
        #
        # pre = self._head
        # new_node = Node(value)
        # not_found = False
        # while pre.next_node != node:
        #     if pre.next_node is None:  # 已到链尾
        #         not_found = True
        #         break
        #     else:
        #         pre = pre.next_node
        #
        # if not not_found:
        #     new_node.next_node = node
        #     pre.next_node = new_node
        dummy = Node(None)
        dummy.next_node = self._head
        pre = dummy
        current = pre.next_node
        while current != node and current is not None:
            pre = current
            current = current.next_node

        if current == node:
            new_node = Node(value)
            new_node.next_node = node
            pre.next_node = new_node
        self._head = dummy.next_node

    def delete_by_value(self, value: int):
        '''
        删除结点中“值等于某个给定值”的结点
        :param value:
        :return:
        '''
        if self._head is None:  # 空链表则什么都不做
            return

        if self._head.data == value:  # 头结点就是待删除的点
            self._head = None
            return
        pre = self._head
        node = pre.next_node
        not_found = False
        while node.data != value:
            if node.next_node is None:  # 到达链尾
                break
            else:

                pre = node
                node = node.next_node
        if not not_found:  # 找到待删除的节点
            pre.next_node = node.next_node

    def delete_by_node(self, node: Node):
        '''
        删除给定指针指向的结点
        :param node:
        :return:
        '''
        if self._head is None or node is None:
            return

        pre = self._head

        while pre.next_node and pre.next_node != node:
            pre = pre.next_node

        if pre.next_node:
            pre.next_node = node.next_node

    def delete_last_n_node(self, n):
        '''
        删除链表中倒数第n个节点，假设N<=链表长度

        利用哨兵简化边界条件
        设置快、慢两个指针，快指针先行，慢指针不动；
        当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
        当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点的前一个节点

        :param n:
        :return:
        '''

        dummy = Node(None)
        dummy.next_node = self._head

        first = dummy
        second = dummy

        for _ in range(n):
            first = first.next_node

        while first.next_node:
            first = first.next_node
            second = second.next_node

        second.next_node = second.next_node.next_node
        self._head = dummy.next_node
        #
        # if n <= 0:
        #     print('n必须大于0')
        #     return
        #
        # if self._head is None:
        #     print('空链表。什么都不做')
        #     return
        #
        # first = self._head
        # second = self._head
        #
        # for _ in range(n):
        #     first = first.next_node
        #
        # if first is None:  # 即要删除的是正数第一个节点，直接将head指向head的下一个节点即可
        #     self._head = self._head.next_node
        #     return
        #
        # while first.next_node:
        #     first = first.next_node
        #     second = second.next_node
        #
        # # 此时first指向倒数第一个节点，假设链表长度为m，则此时first指向第m个节点的前一个节点，
        # # second指向第m-n个节点的前一个节点，也即倒数第m-(m-n)个节点也就是倒数第n个节点的前一个节点
        # # 为了删除倒数第n个节点，则只需将second的下一个节点指向下下个节点
        #
        # second.next_node = second.next_node.next_node
        # return

    def find_mid_node(self):
        '''
        查找链表中的中间节点.
        设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        :return:  如果，链表长度为奇数，则返回的是链表的中间节点，偶数则是后半部分的第一个节点
        '''
        fast = self._head
        slow = self._head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

        return slow

    def find_by_value(self, value: int):
        '''
        根据value查找对应的第一个节点
        :param value:
        :return:
        '''
        p = self._head
        while p and p.data != value:
            p = p.next_node
        return p

    def find_by_index(self, index: int):
        '''
       根据索引查找对应节点
       :param index:
       :return:
       '''
        p = self._head
        pos = 0
        while p and pos != index:
            p = p.next_node
            pos += 1
        return p

    def print_all(self):
        '''
        打印当前链表中所有节点的数据
        :return:
        '''

        pos = self._head
        if pos is None:
            print('链表为空')
            return
        while pos.next_node:
            print(f'{pos.data}-->', end="")
            pos = pos.next_node
        print(pos.data)

    def have_ring(self):
        '''
        检验链表中是否有环
          设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        :return:
        '''
        fast = self._head
        slow = self._head

        while (fast is not None) and (fast.next_node is not None):  # 空链表和单个节点的链表肯定不成环
            fast = fast.next_node.next_node
            slow = slow.next_node
            if fast == slow:
                return True
        return False

    def reverse(self):
        """单链表反转."""
        if self._head is None or self._head.next_node is None:  # 如果链表为空，或者链表只有一个节点
            return

        pre = self._head
        node = self._head.next_node
        while node is not None:  # 条件终止时，pre是最后一个非空节点
            pre, node = self.__reversed_with_two_node(pre, node)

        self._head.next_node = None  # 将原头结点位置（此时已反转方向，应该指向空）的下一个节点指向空
        self._head = pre  # 因为此时pre为反转后的头节点，故头结点指向pre

    @property
    def head_node(self):
        return self._head

    def __reversed_with_two_node(self, pre, node):
        '''
        翻转相邻两个节点
        :param pre: 前一个节点
        :param node: 当前节点
        :return:   (pre,node) 下一个相邻节点的元组
        '''
        tmp = node.next_node
        node.next_node = pre
        pre = node
        node = tmp
        return pre, node

    @staticmethod
    def merge_sorted_list(l1: Node, l2: Node):
        '''
        有序链表合并
        :param p1: 有序链表1的头结点
        :param p2: 有序链表2的头结点
        :return:
        '''
        p1, p2 = l1, l2
        dummy = Node(None)
        current = dummy
        while p1 and p2:
            if p1.data <= p2.data:
                current.next_node = p1
                p1 = p1.next_node
            else:
                current.next_node = p2
                p2 = p2.next_node
            current = current.next_node
        current.next_node = p1 if p1 else p2
        return dummy.next_node


if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.insert_to_head(4)
    l1.insert_to_head(2)
    l1.insert_to_head(1)

    l1.print_all()
    node2 = l1.find_by_index(1)
    l1.insert_node_before(node2, 3)
    l1.print_all()

    l2 = SingleLinkedList()
    l2.insert_to_head(4)
    l2.insert_to_head(3)
    l2.insert_to_head(1)

    l2.print_all()

    l3_head = SingleLinkedList.merge_sorted_list(l1.head_node, l2.head_node)
    current = l3_head
    node_data_list = []
    while current:
        node_data_list.append(str(current.data))
        current = current.next_node
    print('-->'.join(node_data_list))

    l4 = SingleLinkedList()
    for i in range(4):
        l4.insert_to_head(i)

    l4.print_all()
    print(l4.have_ring())
    node3 = l4.find_by_index(0)
    node0 = l4.find_by_value(0)
    node0.next_node = node3  # 成环
    print(l4.have_ring())
