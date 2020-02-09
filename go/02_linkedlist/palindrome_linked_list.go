package linledlist_02

func (l *LinkedList) IsPalindrome() bool {
	head := l.head
	if head == nil || head.next == nil {
		return true
	}

	fast := head.next
	slow := head.next
	realHead := head.next

	for (fast != nil) && (fast.next != nil) {
		fast = fast.next.next
		slow = slow.next
	}

	var pre *Node = nil
	cur := slow

	for cur.next != nil {
		tmp := cur.next
		cur.next = pre
		pre = cur
		cur = tmp
	}

	cur.next = pre
	// 反转了后半段链表

	for cur.next != nil {
		if cur.value != realHead.value {
			return false
		} else {
			cur = cur.next
			realHead = realHead.next
		}
	}
	return cur.value == realHead.value

}
