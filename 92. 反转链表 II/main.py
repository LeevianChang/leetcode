class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode
class Solution:
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next=head
        i = dummy
        count = 0
        while i!=None:
            if count<m-1:
                i = i.next
                count +=1
            else:
                break

        first = i
        i = i.next
        j = i.next
        last = i
        
        count +=1
        while j!=None:
            if count<n:
                tempi = j.next
                tempj = j
                j.next = i
                i = tempj

                j = tempi
                count+=1

            else:
                break
        last.next = j
        first.next = i
        return dummy.next
        





            


s = Solution()
a5 = ListNode(5)
a4 = ListNode(4,a5)
a3 = ListNode(3,a4)
a2 = ListNode(2,a3)
a1 = ListNode(1,a2)

f = s.reverseBetween(a1,1,4)
while f!=None:
    print(f.val)
    f = f.next
# 
 