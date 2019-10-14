# -*- coding: utf-8 -*-

class MyArray:
    '''
    自定义一个int类型型数组，支持顺序插入，往指定位置插入、删除、按下标随机访问
    '''

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, index: int) -> object:
        return self._data[index]

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def __len__(self) -> int:
        return len(self._data)

    def add(self, value: int) -> bool:
        '''
        在数组尾部插入数据.
        :param value:  待插入的值
        :return:
        '''
        if len(self) >= self._capacity:
            return False
        else:
            self._data.append(value)
            return True

    def delete(self, index: int) -> bool:
        '''
         删除数组中指定下标的数据
        :param index: 下标
        :return:
        '''
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        '''
         数组插入数据操作.
        :param index:  将要插入的下标
        :param value: 将要插入的数据
        :return: 插入成功返回True,否则返回False
        '''
        if len(self) >= self._capacity or index < 0:
            return False
        else:
            self._data.insert(index, value)
            return True

    def find(self, index: int) -> object:
        '''
        查找指定下标的数据
        :param index:  下标
        :return: 成功则返回找到的数据，失败返回False
        '''
        try:
            return self._data[index]
        except IndexError:
            return False

    def print_all(self):
        '''打印当前数组所有数据'''
        for value in self:
            print(value)


def test_myarray():
    array = MyArray(5)
    array.add(1)
    array.add(2)
    array.insert(2, 3)
    array.insert(2, 4)
    array.insert(2, 5)
    assert array.insert(0, 6) is False
    assert len(array) == 5
    assert array.find(2) == 5
    assert array.delete(4) is True
    array.print_all()


if __name__ == '__main__':
    test_myarray()
