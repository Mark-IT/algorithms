package _4_queue

import "testing"

func TestLinkedQueue_EnQueue(t *testing.T) {
	l := NewLinkedQueue()
	l.EnQueue(1)
	l.EnQueue(2)
	l.EnQueue(3)
	l.EnQueue(4)
	t.Log(l.Print())
}

func TestLinkedQueue_DeQueue(t *testing.T) {
	l := NewLinkedQueue()
	l.EnQueue(1)
	l.EnQueue(2)
	l.EnQueue(3)
	l.EnQueue(4)

	t.Log(l.Print())
	t.Log(l.DeQueue())
	t.Log(l.Print())
	t.Log(l.DeQueue())
	t.Log(l.Print())
	l.EnQueue(5)
	t.Log(l.Print())
	l.EnQueue(6)
	t.Log(l.Print())
}