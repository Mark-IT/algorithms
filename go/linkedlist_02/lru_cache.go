package linledlist_02

import "fmt"

type LRUNode struct {
	key   interface{}
	value interface{}
	prev  *LRUNode
	next  *LRUNode
}

type LRUCache struct {
	capacity int
	cache    map[int]*LRUNode
	head     *LRUNode
	tail     *LRUNode
	used     int
}

func NewLRUNode(key, value interface{}) *LRUNode {

	return &LRUNode{
		key:   key,
		value: value,
		prev:  nil,
		next:  nil,
	}
}

func NewLRUCache(capacity int) *LRUCache {
	var lruCache LRUCache
	lruCache.cache = make(map[int]*LRUNode, capacity)
	lruCache.capacity = capacity
	lruCache.used = 0

	head := NewLRUNode(nil, nil)
	tail := NewLRUNode(nil, nil)
	head.next = tail
	tail.prev = head
	lruCache.head = head
	lruCache.tail = tail

	//lruCache := LRUCache{
	//	capacity:   capacity,
	//	used:0,
	//	cache: make(map[int]LRUNode, capacity),
	//	head:  nil,
	//	tail:  nil,
	//}
	return &lruCache
}

func (l *LRUCache) InsertHead(node *LRUNode) {
	head := l.head
	head.next.prev = node
	node.next = head.next
	node.prev = head
	head.next = node

}

func (l *LRUCache) Print() {
	cur := l.head.next
	format := ""

	for cur != l.tail {
		format += fmt.Sprintf("%v", cur.value)
		cur = cur.next
		if cur != l.tail {
			format += "->"
		}
	}

	fmt.Println(format)
}

func (l *LRUCache) Get(key int) int {
	curNode, ok := l.cache[key]
	if !ok {
		return -1
	} else {
		curNode.prev.next = curNode.next
		curNode.next.prev = curNode.prev
		l.InsertHead(curNode)
		return l.cache[key].value.(int)
	}
}

func (l *LRUCache) Put(key, value int) {
	curNode, ok := l.cache[key]
	if !ok { // 新节点
		curNode = NewLRUNode(key, value)
		if l.used == l.capacity {
			l.tail.prev.prev.next = l.tail
			l.tail.prev = l.tail.prev.next
			delete(l.cache, key)
		}
		l.InsertHead(curNode)
		l.used++
		l.cache[key] = curNode
		return
	} else {
		curNode.prev.next = curNode.next
		curNode.next.prev = curNode.prev
		l.InsertHead(curNode)

		return
	}
}
