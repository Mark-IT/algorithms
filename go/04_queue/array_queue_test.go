package _4_queue

import "testing"

func TestArrayQueue_Enqueue(t *testing.T) {
	q := NewArrayQueue(5)
	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)
	q.EnQueue(4)
	q.EnQueue(5)
	q.EnQueue(6)
	t.Log(q)
}

func TestArrayQueue_Dequeue(t *testing.T) {
	q := NewArrayQueue(5)
	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)
	q.EnQueue(4)
	q.EnQueue(5)
	q.EnQueue(6)
	t.Log(q)
	t.Log(q.DeQueue())
	t.Log(q)
	t.Log(q.DeQueue())
	t.Log(q)
	t.Log(q.DeQueue())
	t.Log(q)
	t.Log(q.DeQueue())
	t.Log(q)
	t.Log(q.DeQueue())
	t.Log(q)
}

func TestArrayQueue_Print(t *testing.T) {
	q := NewArrayQueue(5)
	q.EnQueue(1)
	q.EnQueue(2)
	q.EnQueue(3)
	q.EnQueue(4)
	q.EnQueue(5)
	q.EnQueue(6)
	t.Log(q.Print())
	q.DeQueue()
	t.Log(q.Print())
	q.DeQueue()
	t.Log(q.Print())
	q.EnQueue(6)
	q.EnQueue(1)
	q.EnQueue(2)
	t.Log(q.Print())
}
