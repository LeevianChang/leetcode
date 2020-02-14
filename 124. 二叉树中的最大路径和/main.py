class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    maxSum = -float("inf")
    def maxPathSum(self, root: TreeNode):
        self.maxPathSumHelper(root)
        return self.maxSum

    def maxPathSumHelper(self,root):
        if root==None:
            return 0
        left = max(self.maxPathSumHelper(root.left),0)
        right = max(self.maxPathSumHelper(root.right),0)
        self.maxSum = max(self.maxSum,left+right+root.val)
        return root.val+max(left,right)
        

rootLeft = TreeNode(9)
rootRight = TreeNode(20,TreeNode(15),TreeNode(7))
root = TreeNode(-10,rootLeft,rootRight)

# rootLeft = TreeNode(9)
# rootRight = TreeNode(20,TreeNode(15),TreeNode(7))
        
s = Solution()
# root = TreeNode(root)


res = s.maxPathSum(root)
print(res)


 