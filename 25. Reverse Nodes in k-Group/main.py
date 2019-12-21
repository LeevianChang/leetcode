# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,nextNode=None):
        self.val = x
        self.next = nextNode


class Solution:
    def reverseKGroup(self, head, k):
        # 判断是否继续
        last = pre = ListNode(0)
        last.next = pre.next = head
        nodeList = []
        for i in range (k):
            if last.next!=None:
                
                nodeList.append(last.next)
                last = last.next
            else:
                return pre.next
        endNode = lastNode = ListNode(0)
        endNode.next= lastNode.next = nodeList.pop()  
        lastNode = lastNode.next
        temp = endNode.next.next
        
        for i in range (k-1):
           

            lastNode.next= nodeList.pop()  
            lastNode = lastNode.next


        lastNode.next =  self.reverseKGroup(temp,k)
        return endNode.next

        
        
a5 = ListNode(5)
a4 = ListNode(4,a5)
a3 = ListNode(3,a4)
a2 = ListNode(2,a3)
a1 = ListNode(1,a2)

s = Solution()
f = s.reverseKGroup(a1,4)

while f!=None:
    
    print(f.val)
    f = f.next

# print(f)