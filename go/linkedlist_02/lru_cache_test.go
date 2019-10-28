package linledlist_02

import (
	"fmt"
	"testing"
)

func TestLRUCache_Put(t *testing.T) {
	lruCache := NewLRUCache(2)
	lruCache.Put(1, 1)
	lruCache.Put(2, 2)
	lruCache.Print()

}

func TestLRUCache_Get(t *testing.T) {
	lruCache := NewLRUCache(2)
	lruCache.Put(1, 1)
	lruCache.Put(2, 2)
	lruCache.Print()
	fmt.Println(lruCache.Get(1))
	lruCache.Print()
	fmt.Println(lruCache.Get(3))

}
