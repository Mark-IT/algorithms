# -*- coding: utf-8 -*-
import unittest
from unittest.mock import patch
from .my_array import MyArray


class TestMyArray(unittest.TestCase):
    def setUp(self):
        self.array = MyArray(5)

    def test_my_array_add(self):
        self.assertEqual(self.array.add(1), True)
        self.assertEqual(self.array.add(2), True)
        self.assertEqual(self.array.add(3), True)
        self.assertEqual(self.array.add(4), True)
        self.assertEqual(self.array.add(5), True)
        self.assertEqual(self.array.add(6), False)

    def test_my_array_capacity(self):
        self.array.add(1)
        self.array.add(2)
        self.array.add(3)
        self.array.add(4)
        self.array.add(5)
        self.array.add(6)
        self.array.add(7)
        self.assertEqual(len(self.array), 5)

    def test_my_array_insert(self):
        self.assertEqual(self.array.insert(0, 1), True)
        self.assertEqual(self.array.insert(0, 2), True)
        self.assertEqual(self.array.insert(0, 3), True)
        self.assertEqual(self.array.insert(0, 4), True)
        self.assertEqual(self.array.insert(0, 5), True)
        self.assertEqual(self.array.insert(0, 6), False)

    def test_my_array_delete(self):
        self.assertEqual(self.array.delete(0), False)
        self.array.add(1)
        self.assertEqual(self.array.delete(0), True)

    def test_my_array_find(self):
        self.array.add(1)
        self.array.add(2)
        self.array.add(3)
        self.assertEqual(self.array.find(0), 1)
        self.assertEqual(self.array.find(2), 3)

    def test_my_array_print_all(self):
        '''
        测试打印值，但是这样只能测试最后打印的一个值是否正确，如果有知道如何同时测试多个打印结果的，烦请告知一下
        :return:
        '''
        self.array.add(1)
        with patch('builtins.print') as mocked_print:
            self.array.print_all()
            mocked_print.assert_called_with(1)
        self.array.add(2)
        with patch('builtins.print') as mocked_print:
            self.array.print_all()
            mocked_print.assert_called_with(2)
        self.array.add(3)
        with patch('builtins.print') as mocked_print:
            self.array.print_all()
            mocked_print.assert_called_with(3)


if __name__ == '__main__':
    unittest.main()
