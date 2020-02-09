package _4_queue

import (
	"fmt"
	"strings"
)

type CircularQueue struct {
	data     []interface{}
	head     int
	tail     int
	capacity int
}

func NewCircularQueue(n int) *CircularQueue {
	return &CircularQueue{make([]interface{}, n), 0, 0, n}
}

// 当队列满时， tail 指向的位置实际上是没有存储数据的。所以，循环队列会浪费一个数组的存储空间。

func (c *CircularQueue) IsFull() bool {
	if c.head == (c.tail+1)%c.capacity {
		return true
	}
	return false
}

func (c *CircularQueue) IsEmpty() bool {
	if c.head == c.tail {
		return true
	}
	return false

}

func (c *CircularQueue) EnQueue(v interface{}) bool {
	if c.IsFull() {
		return false
	}
	c.data[c.tail] = v
	c.tail = (c.tail + 1) % c.capacity
	return true
}

func (c *CircularQueue) DeQueue() interface{} {
	if c.IsEmpty() {
		return nil
	}
	v := c.data[c.head]
	c.head = (c.head + 1) % c.capacity
	return v
}

func (c *CircularQueue) Print() string {

	result := ""

	i := c.head
	for {
		result += fmt.Sprintf("%v->", c.data[i])
		i = (i + 1) % c.capacity
		if i == c.tail {
			break
		}

	}

	result = strings.TrimSuffix(result, "->")
	return result

}
