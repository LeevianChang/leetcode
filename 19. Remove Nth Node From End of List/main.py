# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode

class Solution:
    def removeNthFromEnd(self, head, n):
        preNode = ListNode(0)
        preNode.next = head

        first = preNode
        second = preNode

        for i in range(n):
            if second.next!=None:
                second = second.next
        
        while second.next:
            first = first.next
            second = second.next
        first.next = first.next.next

        return preNode.next
            


        
            






s = Solution()

n5 = ListNode(5)
n4 = ListNode(4,n5)
n3 = ListNode(3,n4)
n2 = ListNode(2,n3)
n1 = ListNode(1,n2)

f = s.removeNthFromEnd(n1,2)
while f:
    print(f.val)

    f = f.next

