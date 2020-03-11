package _5_sorts

func merge(li []int, p, r, q int) {
	i := p
	j := r + 1
	k := 0
	tmpArr := make([]int, q-p+1)
	for ; i <= r && j <= q; k++ {
		if li[i] <= li[j] {
			tmpArr[k] = li[i]
			i++
		} else {
			tmpArr[k] = li[j]
			j++
		}
	}

	for ; i <= r; i++ {
		tmpArr[k] = li[i]
		k++
	}
	for ; j <= q; j++ {
		tmpArr[k] = li[j]
		k++
	}
	copy(li[p:q+1], tmpArr)
}

func mergeSort(li []int, p, q int) {
	if p >= q {
		return
	}
	r := (p + q) / 2
	mergeSort(li, p, r)
	mergeSort(li, r+1, q)
	merge(li, p, r, q)
}

func MergeSort(li []int) {
	mergeSort(li, 0, len(li)-1)
}
