class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root!=None:
            return self.hasPathSumHelper(root,sum-root.val)
        return False
    def hasPathSumHelper(self,root,sum):
        left = right = False
        if root.left!=None:
            remainSum = sum-root.left.val
            if remainSum==0 and root.left.left==None and root.left.right==None:
                left = True
            else:
                left =  self.hasPathSumHelper(root.left,remainSum)

        if root.right!=None:
            remainSum = sum-root.right.val
            if remainSum==0 and root.right.left==None and root.right.right==None:
                right =  True
            else:
                right = self.hasPathSumHelper(root.right,remainSum)

        if root.left==None and root.right==None:
            if sum==0:
                return True
            else:
                return False
        if left or right:

            return True

        return False


    def hasPathSum2(self,root,sum):

        if not root:
            return False
        sum -=root.val
        if not root.left and not root.right:
            return sum==0
        return self.hasPathSum2(root.left,sum) or self.hasPathSum2(root.right,sum)
        

# rootLeft = TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)))
# rootRight = TreeNode(8,TreeNode(13),TreeNode(4,None,TreeNode(1)))
# root = TreeNode(5,rootLeft,rootRight)
        
s = Solution()



res = s.hasPathSum2(TreeNode(-2,None,TreeNode(-3)),-5)
print(res)


 