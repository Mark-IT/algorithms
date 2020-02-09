package linledlist_02

import "fmt"

type Node struct {
	value interface{}
	next  *Node
}

type LinkedList struct {
	head *Node
}

func NewNode(v interface{}) *Node {
	return &Node{v, nil}
}

func NewLinkedList() *LinkedList { // 初始化一个带头结点的链表
	return &LinkedList{NewNode(nil)}
}

//  在某个节点后面插入节点
func (l *LinkedList) InsertNodeAfter(node *Node, value interface{}) bool {

	if node == nil { // 不能在空节点后插入新节点
		return false
	}

	newNode := NewNode(value)
	newNode.next = node.next
	node.next = newNode
	return true

}

//  在某个节点前面面插入节点
func (l *LinkedList) InsertNodeBefore(node *Node, value interface{}) bool {

	if node == nil || node == l.head { // 不能在空节点或头结点前插入新节点
		return false
	}

	pre := l.head
	current := pre.next
	for current != nil && current != node {

		pre = current
		current = current.next
	}

	if current == node {

		newNode := NewNode(value)
		newNode.next = current
		pre.next = newNode
		return true
	}

	return false
}

//在链表头部插入节点
func (l *LinkedList) InsertToHead(value interface{}) bool {
	return l.InsertNodeAfter(l.head, value)
}

// 在链表尾部插入节点
func (l *LinkedList) InsertToTail(value interface{}) bool {
	cur := l.head

	for cur.next != nil {
		cur = cur.next
	}
	return l.InsertNodeAfter(cur, value)

}

// 根据value查找对应的第一个节点
func (l *LinkedList) FindByValue(value interface{}) *Node {
	cur := l.head.next
	for cur != nil && cur.value != value {
		cur = cur.next
	}
	return cur
}

// 根据索引查找对应的节点

func (l *LinkedList) FindByIndex(index int) *Node {
	cur := l.head.next
	pos := 0

	for cur != nil && pos != index {
		cur = cur.next
		pos++
	}
	return cur

}

// 查找链表中间节点
func (l *LinkedList) FindMidNode() *Node {
	// 链表长度为奇数时，返回的是中点，为偶数时，返回的是上半部分的最后一个节点（上中位数）
	fast := l.head
	slow := l.head

	for fast != nil && fast.next != nil {
		fast = fast.next.next
		slow = slow.next
	}
	return slow
}

// 删除指定节点
func (l *LinkedList) DeleteByNode(node *Node) bool {
	cur := l.head
	for cur.next != nil && cur.next != node {
		cur = cur.next
	}
	if cur.next == nil {
		return false
	}
	cur.next = node.next
	return true

}

// 删除节点中 值等于某个指定值的 节点
func (l *LinkedList) DeleteByValue(value interface{}) bool {
	cur := l.head
	for cur.next != nil && cur.next.value != value {
		cur = cur.next
	}
	if cur.next == nil {
		return false
	}
	cur.next = cur.next.next
	return true

}

// 删除倒数第N个节点,假设1<=N<=链表长度

func (l *LinkedList) DeleteBottomN(n int) {

	first := l.head
	second := l.head
	for i := 0; i < n; i++ {
		first = first.next
	}
	for first.next != nil {
		first = first.next
		second = second.next
	}
	second.next = second.next.next
	return
}

// 是否成环
func (l *LinkedList) HaveRing() bool {
	fast := l.head.next
	slow := l.head

	for fast.next != nil && fast.next.next != nil {
		fast = fast.next.next
		slow = slow.next
		if fast == slow {
			return true

		}

	}
	return false

}


// 单链表反转
func (l *LinkedList)  Reverse () {
	var pre  *Node= nil
	cur := l.head.next
	for cur != nil {
		tmp:= cur.next
		cur.next = pre
		pre = cur
		cur = tmp
	}
	l.head.next = pre
	return

}


// 两个有序单链表合并
func MergeSortedList(l1 ,l2 *LinkedList) *LinkedList{
	if l1 == nil || l1.head == nil || l1.head.next == nil{
		return l2
	}
	if l2 == nil || l2.head == nil || l2.head.next == nil{
		return l1
	}

	l :=NewLinkedList()
	p1 := l1.head.next
	p2 := l2.head.next
	cur := l.head
	for p1 != nil && p2 !=nil{
		if p1.value.(int) <=p2.value.(int){
			cur.next = p1
			p1 = p1.next
		}else {
			cur.next = p2
			p2 = p2.next
		}
		cur = cur.next
	}
	if p1 != nil{
		cur.next=p1
	}else {
		cur.next=p2
	}

	return l

}

//打印链表
func (l *LinkedList) Print() {
	cur := l.head.next
	format := ""

	for cur != nil {
		format += fmt.Sprintf("%v", cur.value)
		cur = cur.next
		if cur != nil {
			format += "->"
		}
	}

	fmt.Println(format)
}

