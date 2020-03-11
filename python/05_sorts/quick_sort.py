"""
快速排序
    快排是一种原地、不稳定的排序算法
    快速排序通过设计巧妙的原地分区函数，可以实现原地排序，解决了归并排序占用太多内存的问题
时间复杂度：
    O(nlogn)
    最坏时间复杂度为 O(n2)
        如果数组中的数据原来已经是有序的了，如果我们每次选择最后一个元素作为 pivot，那每次分区得到的两个区间都是不均等的。
        我们需要进行大约 n 次分区操作，才能完成快排的整个过程。
        每次分区我们平均要扫描大约 n/2 个元素，这种情况下，快排的时间复杂度就从 O(nlogn) 退化成了 O(n2)。
空间复杂度：


"""


def partition(li, left, right):
    '''单边循环法'''
    pivot, j = li[left], left  # j指向分区点，选取第一位当做分区点
    for i in range(left + 1, right + 1):  # 从分区点后开始遍历判断
        if li[i] < pivot:
            j += 1
            li[j], li[i] = li[i], li[j]

    # 此时，j指向了pivot应该指向的地方（其左边都比pivot小，右边都比pivot大）
    # pivot所对应的位置已更新完成（指向了j），但是值还在low那里，所以需要将其进行交换
    li[left], li[j] = li[j], li[left]
    return j


def partition2(li, left, right):
    '''双边循环法'''
    pivot = li[left]
    while left < right:
        # 从右往左扫描,直到找到比pivot小的
        while left < right and li[right] >= pivot:
            right -= 1
        li[left] = li[right]  # 找到小的，right位置空出了
        # 从左往右扫描,直到找到比pivot大的
        while left < right and li[left] <= pivot:
            left += 1
        li[right] = li[left]  # 找到大的，填补right,left空出
    li[left] = pivot  # 分区点归位
    return left


def quick_sort(li):
    _quick_sort(li, 0, len(li) - 1)


def _quick_sort(li, left, right):
    if left < right:
        p = partition(li, left, right)
        # p = partition2(li, left, right)
        _quick_sort(li, left, p - 1)
        _quick_sort(li, p + 1, right)


def test_quick_sort():
    a1 = [3, 5, 6, 7, 8]
    quick_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    quick_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    quick_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)
