package _4_queue

import "testing"

func TestCircularQueue_EnQueue(t *testing.T) {
	l := NewCircularQueue(3)
	t.Log(l.EnQueue(1))
	t.Log(l.EnQueue(2))
	t.Log(l.EnQueue(3))
	t.Log(l.EnQueue(4))
	t.Log(l.Print())
}

func TestCircularQueue_DeQueue(t *testing.T) {
	l := NewCircularQueue(3)
	l.EnQueue(1)
	l.EnQueue(2)
	l.EnQueue(3)
	l.EnQueue(4)

	t.Log(l.Print())
	t.Log(l.DeQueue())
	t.Log(l.Print())
	t.Log(l.DeQueue())
	t.Log(l.Print())
	t.Log(l.EnQueue(5))
	t.Log(l.Print())
	t.Log(l.EnQueue(6))
	t.Log(l.Print())
}