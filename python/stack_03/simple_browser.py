# -*- coding: utf-8 -*-
import sys

sys.path.append('linked_stack.py')

from linked_stack import LinkedStack


class Browser():
    '''
    使用两个栈模拟浏览器前进后退
    '''

    def __init__(self):
        self.forward_stack = LinkedStack()
        self.back_stack = LinkedStack()

    def can_forward(self):
        if self.back_stack.is_empty():
            return False

        return True

    def can_back(self):
        if self.forward_stack.is_empty():
            return False

        return True

    def open(self, url):
        print(f"打开新地址： {url}")
        self.forward_stack.push(url)

    def back(self):
        if self.forward_stack.is_empty():
            return

        top = self.forward_stack.pop()
        self.back_stack.push(top)
        print(f"后退至： {top}")

    def forward(self):
        if self.back_stack.is_empty():
            return

        top = self.back_stack.pop()
        self.forward_stack.push(top)
        print(f"前进至： {top}")


if __name__ == '__main__':

    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()
