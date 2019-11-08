package stack_03

import (
	"fmt"
)

type ArrayStack struct {
	top  int
	data [] interface{} //	 存放数据
}

func NewArrayStack() *ArrayStack {
	return &ArrayStack{
		top:  -1,
		data: make([] interface{}, 0, 8),
	}
}

func (s *ArrayStack) IsEmpty() bool {
	return s.top == -1
}

func (s *ArrayStack) Push(value interface{}) {

	if len(s.data)+1 <= cap(s.data) {
		fmt.Println("入栈")
		s.top += 1
		s.data = append(s.data, value)

	} else {
		fmt.Println("栈已满，无法入栈")
	}

}

func (s *ArrayStack) Pop() interface{} {
	if s.IsEmpty() {
		fmt.Print("栈已空，无法出栈")
		return nil
	} else {
		fmt.Println("出栈")
		v := s.data[s.top]
		s.top -= 1
		return v

	}
}

func (s *ArrayStack) Print() {
	if s.IsEmpty() {
		fmt.Println("空栈")
	} else {
		fmt.Println("栈中剩余数据，出栈顺序为：")
		for i :=s.top ; i >= 0; i-- {
			fmt.Println(s.data[i])
		}
	}
}
