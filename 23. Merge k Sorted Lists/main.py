class ListNode:
    def __init__(self, x,nextNode = None):
        self.val = x
        self.next = nextNode

class Solution:
    def mergeKLists(self, lists):

        if len(lists)==0:
            return ListNode(0).next
        self.part(lists,0,len(lists)-1)

        return lists[0]

    def part(self,lists,start,end):
        interval = 1
        
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge(lists[i],lists[i+interval])
            interval *= 2
        return lists[0] if amount > 0 else lists
        
       

    def merge(self,list1,list2):
        head = pre = ListNode(0)
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                pre.next = list1
                list1 = list1.next
            else:
                pre.next = list2
                
                list2 = list2.next
            pre = pre.next
        
        if list1==None:
            pre.next = list2
        else:
            pre.next = list1
        # print(head.next.val)
        return head.next
        
        

        
        




            
        
            
s = Solution()


a1 = ListNode(1)

b5 = ListNode(5)
b1 = ListNode(-1,b5)


c6 = ListNode(6)
c4 = ListNode(4)
c1 = ListNode(1,c4)

d6 = ListNode(6)
d5 = ListNode(5,d6)
d4 = ListNode(4,d6)

f = s.mergeKLists([a1.next,b1,c1,d4])
while f!=None:
    
    print(f.val)
    f = f.next

# print(f)