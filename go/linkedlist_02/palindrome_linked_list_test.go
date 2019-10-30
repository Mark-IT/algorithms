package linledlist_02

import (
	"fmt"
	"testing"
)

func TestIsPalindrome(t *testing.T) {

	l := NewLinkedList()
	fmt.Println("", l.IsPalindrome())

	l1Str := "a"
	l1 := NewLinkedList()

	for _, i := range l1Str {
		l1.InsertToTail(i)

	}

	fmt.Println(l1Str, l1.IsPalindrome())

	l2Str := "aa"
	l2 := NewLinkedList()

	for _, i := range l2Str {
		l2.InsertToTail(i)

	}

	fmt.Println(l2Str, l2.IsPalindrome())

	l3Str := "aba"
	l3 := NewLinkedList()

	for _, i := range l3Str {
		l3.InsertToTail(i)

	}

	fmt.Println(l3Str, l3.IsPalindrome())

	l4Str := "abc"
	l4 := NewLinkedList()

	for _, i := range l4Str {
		l4.InsertToTail(i)

	}

	fmt.Println(l4Str, l4.IsPalindrome())

	l5Str := "abcd"
	l5 := NewLinkedList()

	for _, i := range l5Str {
		l5.InsertToTail(i)

	}

	fmt.Println(l5Str, l5.IsPalindrome())

	l6Str := "上海自来水来自海上"
	l6 := NewLinkedList()

	for _, i := range l6Str {
		l6.InsertToTail(i)

	}

	fmt.Println(l6Str, l6.IsPalindrome())
}
