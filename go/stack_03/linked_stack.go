package stack_03

import "fmt"

type Node struct {
	val  interface{}
	next *Node
}

type LinkedStack struct {
	topNode *Node
}

func NewLinkedStack() *LinkedStack {
	return &LinkedStack{nil}
}

func (s *LinkedStack) IsEmpty() bool {
	return s.topNode == nil
}

func (s *LinkedStack) Push(value interface{}) {
	fmt.Println("入栈")
	s.topNode = &Node{value, s.topNode}
}

func (s *LinkedStack) Pop() interface{} {
	fmt.Println("出栈")

	if s.IsEmpty() {
		return nil
	}
	v := s.topNode.val
	s.topNode = s.topNode.next
	return v
}

func (s *LinkedStack) Print() {
	if s.IsEmpty() {
		fmt.Println("空栈")
	} else {
		fmt.Println("栈中剩余数据，出栈顺序为：")
		cur := s.topNode
		for cur != nil {
			fmt.Println(cur.val)
			cur = cur.next
		}

	}
}
