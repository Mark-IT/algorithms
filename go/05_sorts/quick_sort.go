package _5_sorts

func partition(li []int, left, right int) int {
	pivot, j := li[left], left
	for i := left + 1; i <= right; i++ {
		if li[i] < pivot {
			j++
			li[j], li[i] = li[i], li[j]
		}
	}
	li[left], li[j] = li[j], li[left]
	return j

}

func quickSort(li []int, left, right int) {
	if left >= right {
		return
	}
	p := partition(li, left, right)
	quickSort(li, left, p-1)
	quickSort(li, p+1, right)
}

func QuickSort(li []int) {
	quickSort(li, 0, len(li)-1)
}
