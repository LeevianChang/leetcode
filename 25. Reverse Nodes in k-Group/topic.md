## 25. Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.

>Link:https://leetcode-cn.com/problems/reverse-nodes-in-k-group


## Train of Thought
此题为24题的升级版，使用了递归的方式，先判断当先的节点后续的节点能否构成k个，并插入列表中，如果不能，跳出递归结束
如果可以，则从列表中pop出节点，实现节点倒置链接