class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        if p.val!=q.val:
            return False
        

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        

s = Solution()

pLeft = TreeNode(5)
pRight = TreeNode(15)
p = TreeNode(10,pLeft,pRight)


q1Right = TreeNode(15)
qLeft = TreeNode(5,None,q1Right)
# qRight = TreeNode(1)
q = TreeNode(10,qLeft)
res = s.isSameTree(p,q)


print(res)

 