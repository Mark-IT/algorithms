package _5_sorts

import (
	"fmt"
	"testing"
)

func TestBubbleSort(t *testing.T) {
	arr := []int{1,5,9,6,3,7,5,10}
	fmt.Println("排序前：",arr)
	BubbleSort(arr)
	fmt.Println("排序后：",arr)
}

func TestInsertSort(t *testing.T) {
	arr := []int{1,5,9,6,3,7,5,10}
	fmt.Println("排序前：",arr)
	InsertSort(arr)
	fmt.Println("排序后：",arr)
}

func TestSelectSort(t *testing.T) {
	arr := []int{1,5,9,6,3,7,5,10}
	fmt.Println("排序前：",arr)
	SelectSort(arr)
	fmt.Println("排序后：",arr)
}