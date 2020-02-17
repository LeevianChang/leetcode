class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return self.isMirror(root.left,root.right)


    def isMirror(self,p,q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        if p.val!=q.val:
            return False
        else:
            return self.isMirror(p.left,q.right) and self.isMirror(p.right,q.left) 
s = Solution()


q2left = TreeNode(4)
q2Right = TreeNode(3)
q1left = TreeNode(3)
q1Right = TreeNode(4)
qLeft = TreeNode(2,q1left,q1Right)
qright = TreeNode(2,q2left,q2Right)
# qRight = TreeNode(1)
q = TreeNode(1,qLeft,qright)


# q2left = TreeNode(2)

# q1left = TreeNode(2)
# q1Right = TreeNode(2)
# qLeft = TreeNode(2,q1left)
# qright = TreeNode(2,q2left)
# # qRight = TreeNode(1)
# q = TreeNode(1,qLeft,qright)
res = s.isSymmetric(q)


print(res)

 