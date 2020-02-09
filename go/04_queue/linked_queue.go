package _4_queue

import (
	"fmt"
	"strings"
)

// 基于链表的队列

type Node struct {
	value interface{}
	next  *Node
}

type LinkedQueue struct {
	head   *Node
	tail   *Node
	length int
}

func NewNode(v interface{}) *Node {
	return &Node{v, nil}
}

func NewLinkedQueue() *LinkedQueue {
	return &LinkedQueue{nil, nil, 0}
}

func (l *LinkedQueue) EnQueue(v interface{}) {
	newNode := NewNode(v)
	if l.tail == nil {
		l.head = newNode
		l.tail = newNode
	} else {
		l.tail.next = newNode
		l.tail = newNode
	}
	l.length++

}

func (l *LinkedQueue) DeQueue() interface{} {
	if l.head == nil {
		return nil
	}

	v := l.head.value
	l.head = l.head.next
	l.length--
	return v

}


func (l *LinkedQueue) Print() string{
	cur:=l.head
	result:=""
	for cur != nil{
		result+=fmt.Sprintf("%v->",cur.value)
		cur = cur.next
	}
	result = strings.TrimSuffix(result,"->")
	return result
}
