class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode
class Solution:
    
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(0)
        dummy2 = ListNode(0)
        q = dummy2
        dummy.next = head
        i = dummy
        j = dummy.next
        while j:
            if j.val<x:
            
                i.next = j

                i = i.next 
                j = j.next

            else:

                q.next = j
                j = j.next

                q = q.next
        q.next=None
        
        i.next = dummy2.next

        return dummy.next

        

s = Solution()
a6 = ListNode(2)
a5 = ListNode(5,a6)
a4 = ListNode(2,a5)
a3 = ListNode(3,a4)
a2 = ListNode(4,a3)
a1 = ListNode(1,a2)

f = s.partition(a1,3)
while f!=None:
    print(f.val)
    f = f.next
# 
 