class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def maxDepth(self, root: TreeNode) -> int:
        
        return self.maxDepthHelper(root)

    def maxDepthHelper(self,root):
        if root==None:
            return 0

      
        left = self.maxDepthHelper(root.left)+1
       
        right = self.maxDepthHelper(root.right)+1

        return max(left,right)
        
        


        
s = Solution()

p1left =  TreeNode(15)
p1right =  TreeNode(7)
pLeft = TreeNode(20,p1left,p1right)
pRight = TreeNode(9)
p = TreeNode(3,pLeft,pRight)

res = s.maxDepth(p)


print(res)

 