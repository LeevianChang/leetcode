class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode
class Solution:
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head==None or head.next==None:
            return head
        dummy = ListNode("-1")
        dummy.next=head
        slow = head
        fast = head
        while fast:
            while fast.next and slow.val==fast.next.val:
                fast = fast.next
            if fast.next:
                slow.next = fast.next
                slow = slow.next
                
            fast = fast.next
        slow.next=None

        return dummy.next

        

s = Solution()
a7 = ListNode(5)
a6 = ListNode(3,a7)
a5 = ListNode(3,a6)
a4 = ListNode(2,a5)
a3 = ListNode(2,a4)
a2 = ListNode(1,a3)
a1 = ListNode(1,a2)

f = s.deleteDuplicates(a1)
while f!=None:
    print(f.val)
    f = f.next
# print(f.val)
# 
 