## 19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Link：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list


## Train of Thought

使用两个指针，两个指针的间隔是n，同时移动两个指针向前移动，前面的指针指向尾部时，后一个指针指向的next即为需要移除的node