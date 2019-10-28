package linledlist_02

import (
	"fmt"
	"testing"
)

func TestLinkedList_InsertToHead(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 10; i++ {
		l.InsertToHead(i + 1)
	}
	l.Print()
}
func TestInsertToTail(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 10; i++ {
		l.InsertToTail(i + 1)
	}
	l.Print()
}

func TestFindByIndex(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 10; i++ {
		l.InsertToTail(i + 1)
	}
	t.Log(l.FindByIndex(0))
	t.Log(l.FindByIndex(9))
	t.Log(l.FindByIndex(5))
	t.Log(l.FindByIndex(11))
}

func TestDeleteNode(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 3; i++ {
		l.InsertToTail(i + 1)
	}
	l.Print()

	t.Log(l.DeleteByNode(l.head.next))
	l.Print()

	t.Log(l.DeleteByNode(l.head.next.next))
	l.Print()
}

func TestLinkedList_DeleteBottomN(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 10; i++ {
		l.InsertToTail(i + 1)
	}
	l.Print()
	l.DeleteBottomN(1)
	l.Print()
}

func TestLinkedList_HaveRing(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 10; i++ {
		l.InsertToTail(i + 1)
	}
	fmt.Println(l.HaveRing())
	lastNode := l.FindByValue(10)
	lastNode.next = l.head
	fmt.Println(l.HaveRing())
}

func TestLinkedList_Reverse(t *testing.T) {
	l := NewLinkedList()
	for i := 0; i < 10; i++ {
		l.InsertToTail(i + 1)
	}
	l.Print()
	l.Reverse()
	l.Print()

}

func TestMergeSortedList(t *testing.T) {
	l1 := NewLinkedList()
	for i := 0; i < 5; i++ {
		l1.InsertToTail(i + 1)
	}
	l1.Print()
	l2 := NewLinkedList()
	for i := 5; i < 10; i++ {
		l2.InsertToTail(i + 1)
	}
	l2.Print()
	l := MergeSortedList(l1, l2)
	l.Print()
}

func TestLinkedList_FindMidNode(t *testing.T) {
	l1 := NewLinkedList()
	for i := 0; i < 5; i++ {
		l1.InsertToTail(i + 1)
	}
	l1.Print()
	fmt.Println(l1.FindMidNode())

	l2 := NewLinkedList()
	for i := 0; i < 4; i++ {
		l2.InsertToTail(i + 1)
	}
	l2.Print()
	fmt.Println(l2.FindMidNode())
}
