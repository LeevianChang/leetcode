class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:

    def minDepth(self, root: TreeNode) -> int:
        return self.minDepthHelper(root)
        
        
    def minDepthHelper(self,root):
        if root==None:
            return 0
        if root.left==None and  root.right==None:
            return 1
        minDeep = float('inf')
        if root.left!=None:
            minDeep = min(self.minDepthHelper(root.left),minDeep)
        if root.right!=None:
        
            minDeep = min(self.minDepthHelper(root.right),minDeep)
        return minDeep+1
        

        
    

      


        


p1left =  TreeNode(15,TreeNode(1,TreeNode(1,TreeNode(2))))
p1right =  TreeNode(7)
pLeft = TreeNode(20,p1left,p1right)
pRight = TreeNode(9)
p = TreeNode(3,pLeft,pRight)
        
s = Solution()



res = s.minDepth(p)
print(res)


 