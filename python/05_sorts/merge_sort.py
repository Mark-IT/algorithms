"""
归并排序

时间复杂度：
    归并排序不关心数组的初始状态，因此最好、最坏、平时时间复杂度都是一样的，为O(nlogn)
空间复杂度为 :
    尽管每次合并操作都需要申请额外的内存空间，但在合并完成之后，临时开辟的内存空间就被释放掉了。
    在任意时刻，CPU 只会有一个函数在执行，也就只会有一个临时的内存空间在使用。
    临时内存空间最大也不会超过 n 个数据的大小，所以空间复杂度是 O(n)
稳定性：
    稳定。我们对数组分成左右两部分，对于两边相同的值，我们可以选择将右部分的值归并后放在左边相同值的后面，因此它是稳定的排序算法

归并排序虽然是稳定的、时间复杂度为 O(nlogn) 的排序算法，但是它是非原地排序算法。归并之所以是非原地排序算法，主要原因是合并函数无法在原地执行
缺点占用内存
"""


def merge(li, p, r, q):
    """
    归并函数,排序并合并
    例如 li[p:q] = [...,1,4,2,3,...]
    li[p:r] = [1,4]
    li[r:q] = [2,3]
    tmp = [1,2,3,4]
    归并后 li[p:q] = [...,1,2,3,4,...]
    :param li:子数组
    :param p:当前数组的首下标
    :param r:当前数组的中位下标
    :param q:当前数组的尾下标
    :return:
    """
    i = p
    j = r + 1
    tmp = []

    while i <= r and j <= q:
        if li[i] <= li[j]:
            tmp.append(li[i])
            i += 1
        else:
            tmp.append(li[j])
            j += 1
    while i <= r:
        tmp.append(li[i])
        i += 1
    while j <= q:
        tmp.append(li[j])
        j += 1
    # 此时tmp中已排好序，回填到子数组中
    li[p:q + 1] = tmp


def _merge_sort(li, p, q):
    '''

    :param li: 原数组
    :param p: 当前数组的首下标
    :param q: 当前数组的尾下标
    :return:
    '''
    if p >= q:
        return
    # 取中间值
    r = (p + q) // 2
    # 将数组分成左部分li[p:r]和右部分li[r+1,q],左右部分递归调用分解
    _merge_sort(li, p, r)
    _merge_sort(li, r + 1, q)
    # 归并左右部分的结果，将li[p:r]和li[r+1,q]按顺序归并到li中相应的位置
    merge(li, p, r, q)


def merge_sort(li):
    '''
    归并排序，先分解排序，再合并
    归并排序的处理过程是由下到上的，先处理子问题，然后再合并

    :param li:待排序的数组
    :return:
    '''
    _merge_sort(li, 0, len(li) - 1)


def test_merge_sort():
    a1 = [3, 5, 6, 7, 8]
    merge_sort(a1)
    assert a1 == [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    merge_sort(a2)
    assert a2 == [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    merge_sort(a3)
    assert a3 == [1, 2, 3, 4]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a4)
    assert a4 == [-2, -1, 3, 3, 5, 7, 8, 9, 9]


if __name__ == "__main__":
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)
