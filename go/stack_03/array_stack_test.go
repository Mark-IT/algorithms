package stack_03

import (
	"fmt"
	"testing"
)

func TestArrayStack_Push(t *testing.T) {
	s := NewArrayStack()
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	s.Print()
}


func TestArrayStack_Pop(t *testing.T) {
	s := NewArrayStack()
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
	s.Print()
}