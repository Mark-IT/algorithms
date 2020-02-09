package _3_stack

import (
	"fmt"
	"testing"
)

func TestLinkedStack_Push(t *testing.T) {
	s := NewLinkedStack()
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	s.Print()
}


func TestLinkedStack_Pop(t *testing.T) {
	s := NewLinkedStack()
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
	s.Print()
}