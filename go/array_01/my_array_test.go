package array_01

import (
	"testing"
)

func TestArray_Insert(t *testing.T) {
	capacity := 5
	arr := NewArray(capacity)
	for i := 0; i < capacity-2; i++ {
		err := arr.Insert(i, i+1)
		if nil != err {
			t.Fatal(err.Error())
		}
	}
	arr.PrintAll()

	arr.Insert(3, 999)
	arr.PrintAll()

	arr.InsertToTail(666)
	arr.PrintAll()

}

func TestArray_Delete(t *testing.T) {
	capacity := 5
	arr := NewArray(capacity)
	for i := 0; i < capacity; i++ {
		err := arr.Insert(i, i+1)
		if nil != err {
			t.Fatal(err.Error())
		}
	}
	arr.PrintAll()

	arr.Delete(0)
	arr.PrintAll()
	arr.Delete(2)
	arr.PrintAll()
}

func TestArray_Find(t *testing.T) {
	capacity := 5
	arr := NewArray(capacity)
	for i := 0; i < capacity; i++ {
		err := arr.Insert(i, i+1)
		if nil != err {
			t.Fatal(err.Error())
		}
	}

	t.Log(arr.Find(0))
	t.Log(arr.Find(4))
	t.Log(arr.Find(6))

}
