class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode
class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head

        dummy = ListNode("a")
        dummy.next=head
        slow = dummy
        fast = dummy.next
        while fast:
            while fast.next and slow.next.val==fast.next.val:
                fast = fast.next
            if slow.next ==fast:
                slow = fast
            else:
                slow.next = fast.next
            fast = fast.next



        
        return dummy.next

    


s = Solution()
a7 = ListNode(5)
a6 = ListNode(4,a7)
a5 = ListNode(4,a6)
a4 = ListNode(3,a5)
a3 = ListNode(3,a4)
a2 = ListNode(2,a3)
a1 = ListNode(1,a2)

f = s.deleteDuplicates(a1)
while f!=None:
    print(f.val)
    f = f.next
# print(f.val)
# 
 