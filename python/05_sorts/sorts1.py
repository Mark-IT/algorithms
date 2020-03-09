"""
排序算法的稳定性：
如果待排序的序列中存在值相等的元素，经过排序之后，相等元素之间原有的先后顺序不变，则称这种算法是稳定的

排序算法的内存消耗：
原地排序算法，就是特指空间复杂度是 O(1) 的排序算法

    Bubble sort, insertion sort and selection sort
    冒泡排序、插入排序、选择排序都是基于元素交换或移动的原地排序算法

"""


# 冒泡排序
def bubble_sort(li: list):
    '''
    思路：
        列表每两个相邻的数比较大小，如果前边的比后边的大，那么这两个数就互换位置。就像是冒泡一样，执行n-1趟即可，n代表列表长度

    只涉及相邻数据的交换操作，只需要常量级的临时空间，所以它的空间复杂度为 O(1)，是一个原地排序算法
    当有相邻的两个元素大小相等的时候，我们不做交换，相同大小的数据在排序前后不会改变顺序，所以冒泡排序是稳定的排序算法
    最好情况下，要排序的数据已经是有序的了，我们只需要进行一次冒泡操作，就可以结束了，所以最好情况时间复杂度是 O(n)
    最坏的情况是，要排序的数据刚好是倒序排列的，我们需要进行 n 次冒泡操作，所以最坏情况时间复杂度为 O(n2)
    平均时间复杂度为O(n2)
    注：n2这里是指n的2次方
    :param li:
    :return:
    '''
    for i in range(len(li) - 1):  # 趟数
        change = False
        for j in range(len(li) - i - 1):

            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                change = True
        if not change:
            return


def insert_sort(li: list):
    '''
    思路：
        首先，我们将数组中的数据分为两个区间，已排序区间和未排序区间。
        初始已排序区间只有一个元素，就是数组的第一个元素。
        插入算法的核心思想是取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入，并保证已排序区间数据一直有序。
        重复这个过程，直到未排序区间中元素为空，算法结束

    插入排序算法的运行并不需要额外的存储空间，所以空间复杂度是 O(1)，也就是说，这是一个原地排序算法
    在插入排序中，对于值相同的元素，我们可以选择将后面出现的元素，插入到前面出现元素的后面，这样就可以保持原有的前后顺序不变，所以插入排序是稳定的排序算法
    如果要排序的数据已经是有序的，我们并不需要搬移任何数据。如果我们从尾到头在有序数据组里面查找插入位置，每次只需要比较一个数据就能确定插入的位置。所以这种情况下，最好是时间复杂度为 O(n)。注意，这里是从尾到头遍历已经有序的数据
    如果数组是倒序的，每次插入都相当于在数组的第一个位置插入新的数据，所以需要移动大量的数据，所以最坏情况时间复杂度为 O(n2)
    在数组中插入一个数据的平均时间复杂度是O(n)，所以，对于插入排序来说，每次插入操作都相当于在数组中插入一个数据，循环执行 n 次插入操作，所以平均时间复杂度为 O(n2)
    :param li:
    :return:
    '''

    for i in range(1, len(li)):  # 无序区，i表示摸到的牌的序号
        tmp = li[i]
        j = i - 1  # 指向有序区最后一个位置，也就是目前手里最大的牌的序号
        while j >= 0 and li[j] > tmp:  # 当前抽到的牌比手里最大的牌小，要移动有序区的牌，给它挪位置
            li[j + 1] = li[j]
            j -= 1
        # 移动完毕后j所在位置是有序区里最小的，比当前抽到的牌还小的牌，所在位置，所以将新牌插入其后
        li[j + 1] = tmp


def select_sort(li: list):
    '''
    思路：
        一趟遍历完记录最小的数，放到第一个位置；在一趟遍历记录剩余列表中的最小的数，继续放置

    选择排序空间复杂度为 O(1)，是一种原地排序算法。
    选择排序的最好情况时间复杂度、最坏情况和平均情况时间复杂度都为 O(n2)

    :param li:
    :return:
    '''
    for i in range(len(li) - 1):  # 趟数
        min_loc = i  # 最小数的位置
        for j in range(min_loc + 1, len(li)):  # 两个位置进行比较，如果后面的一个比最小的那个位置还小，说明就找到最小的了
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]  # 把找到的两个值进行互换位置


def test_bubble_sort():
    test_array = [1, 1, 1, 1]
    bubble_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    bubble_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_insertion_sort():
    test_array = [1, 1, 1, 1]
    insert_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    insert_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    insert_sort(test_array)
    assert test_array == [1, 2, 3, 4]


def test_selection_sort():
    test_array = [1, 1, 1, 1]
    select_sort(test_array)
    assert test_array == [1, 1, 1, 1]
    test_array = [4, 1, 2, 3]
    select_sort(test_array)
    assert test_array == [1, 2, 3, 4]
    test_array = [4, 3, 2, 1]
    select_sort(test_array)
    assert test_array == [1, 2, 3, 4]


if __name__ == "__main__":
    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    bubble_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    insert_sort(array)
    print(array)

    array = [5, 6, -1, 4, 2, 8, 10, 7, 6]
    select_sort(array)
    print(array)
