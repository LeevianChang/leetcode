# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode


class Solution:
    def swapPairs(self, head):
        last = pre = ListNode(0)
        last.next = pre.next = head
        while last.next!=None and last.next.next!=None:
            first = last.next
            second = first.next
            third = second.next
            
            first.next = third
            second.next = first
            last.next = second
            
            last = first

        
        return pre.next

a4 = ListNode(4)
a3 = ListNode(3,a4)
a2 = ListNode(2,a3)
a1 = ListNode(1,a2)

s = Solution()
f = s.swapPairs(a1)

while f!=None:
    
    print(f.val)
    f = f.next

# print(f)