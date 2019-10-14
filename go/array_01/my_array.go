package array_01

import (
	"errors"
	"fmt"
)

type Array struct {
	data   [] int
	length int
}

// 初始化数组
func NewArray(capacity int) *Array {
	if capacity == 0 {
		return nil
	}
	return &Array{
		data:   make([]int, capacity, capacity),
		length: 0,
	}
}

//判断索引是否越界
func (a *Array) isIndexOutOfRange(index int) bool {
	if index >= a.length {
		return true
	}
	return false
}

//插入数值到索引index上
func (a *Array) Insert(index int, value int) error {
	if a.length == cap(a.data) {
		return errors.New("full array")
	}
	if index != a.length && a.isIndexOutOfRange(index) {
		return errors.New("out of index range")
	}
	// 如果当前插入位置不在最后，则需要把此位置后面的元素整体后移
	for i := a.length; i > index; i-- {
		a.data[i] = a.data[i-1]
	}
	a.data[index] = value
	a.length++
	return nil

}

// 从尾部插入
func (a *Array) InsertToTail(value int) error {
	return a.Insert(a.length, value)
}

//通过索引查找数组，索引范围[0,n-1]
func (a *Array) Find(index int) (int, error) {
	if a.isIndexOutOfRange(index) {
		return -1, errors.New("out of index range")

	}
	return a.data[index], nil
}

// 删除指定索引位置的值
func (a *Array) Delete(index int) error {
	if a.isIndexOutOfRange(index) {
		return errors.New("out of index range")
	}
	// 删除，后续元素前移
	for i := index; i < a.length-1; i++ {
		a.data[i] = a.data[i+1]
	}
	a.length--
	return nil
}

func (a *Array) PrintAll() {
	fmt.Println(a.data)
	//for i:=0;i<a.length;i++ {
	//
	//}
}
