class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    res = True

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)!=-1
        
        

    def isBalancedHelper(self,root):
        if root==None:
            return 0

        left = self.isBalancedHelper(root.left)
        if left==-1:
            return -1
        right = self.isBalancedHelper(root.right)
        if right==-1:
            return -1
        if abs(right-left)>1:
         
            return -1
        else:
            return max(left+1,right+1)
        
        
        
      


        


p1left =  TreeNode(15,TreeNode(1,TreeNode(1,TreeNode(2))))
p1right =  TreeNode(7)
pLeft = TreeNode(20,p1left,p1right)
pRight = TreeNode(9)
p = TreeNode(3,pLeft,pRight)
        
s = Solution()



res = s.isBalanced(p)
print(res)


 