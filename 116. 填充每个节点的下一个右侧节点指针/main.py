class TreeNode:
    def __init__(self, x,left = None,right = None,next = None):
        self.val = x
        self.left = left
        self.right = right
        self.next = next
class Solution:

    def connect(self, root) :
        queue = []
        queue.append(root)
        queue.append(None)

        while root and len(queue)>0:
            pop = queue.pop(0)
            if pop!=None:
                pop.next = queue[0]
                if pop.left!=None:
                    queue.append(pop.left)
                if pop.right!=None:
                    queue.append(pop.right)
                
            else:
                if len(queue)>0:
                    queue.append(None)


        return root



            
        


pLeft =  TreeNode(2,TreeNode(4),TreeNode(5))
pRight =  TreeNode(3,TreeNode(6),TreeNode(7))
p = TreeNode(1,pLeft,pRight)
        
s = Solution()



res = s.connect(p)
print(res.left.right.next.val)


 