package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || k == 0 {
		return head
	}
	length := 1
	start := head
	for head.Next != nil {
		length += 1
		head = head.Next
	}
	head.Next = start
	move := 0
	if length > k {
		move = length - k
	} else {
		move = length - k%length
	}

	endNode := start
	i := 0
	for start.Next != nil {
		i += 1
		if i != move {
			endNode = endNode.Next

			start = start.Next

		} else {
			break
		}
	}
	// fmt.Println(endNode.Val)

	preHead := endNode.Next
	endNode.Next = nil
	return preHead

}

func main() {
	a5 := ListNode{Val: 5, Next: nil}
	a4 := ListNode{Val: 4, Next: &a5}
	a3 := ListNode{Val: 3, Next: &a4}
	a2 := ListNode{Val: 2, Next: &a3}
	a1 := ListNode{Val: 1, Next: &a2}
	// a0 := ListNode{Val: 0, Next: nil}
	n := rotateRight(&a1, 0)
	for n.Next != nil {
		fmt.Println(n.Val)
		n = n.Next

	}
	fmt.Println(n.Val)

}
