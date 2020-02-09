package _4_queue

import (
	"fmt"
)

// 基于数组的队列
type ArrayQueue struct {
	data     []interface{}
	capacity int
	head     int
	tail     int
}

func (q *ArrayQueue) EnQueue(v interface{}) bool {
	if q.tail == q.capacity {
		if q.head == 0 {
			return false
		} else { // 队列中前面有空的位置,进行数据搬移

			for i := 0; i < q.tail-q.head; i++ {
				q.data[i] = q.data[i+q.head]
			}
			// 搬移完成后，修改头尾指针指向
			q.tail -= q.head
			q.head = 0
		}

	}

	q.data[q.tail] = v
	q.tail++
	return true
}

func (q *ArrayQueue) DeQueue() interface{} {
	if q.head == q.capacity {
		return nil
	}
	v := q.data[q.head]
	q.head++
	return v
}

func (q *ArrayQueue) Print() string {


	result := ""
	for i := q.head; i < q.tail-1; i++ {
		result += fmt.Sprintf("%v->", q.data[i])
	}
	result += fmt.Sprintf("%v", q.data[q.tail-1])
	return result


}

func NewArrayQueue(n int) *ArrayQueue {
	return &ArrayQueue{make([]interface{}, n), n, 0, 0}
}
