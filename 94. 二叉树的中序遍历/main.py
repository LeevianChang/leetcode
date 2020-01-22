class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    
    def inorderTraversal(self, root: TreeNode):
        res = []
        if root!=None:
            self.inorderTraversalHelper(root,res)
        return res
    

    def inorderTraversalHelper(self,root,res):
        if root.left!=None:
            self.inorderTraversalHelper(root.left,res)

        res.append(root.val)

        if root.right!=None:
            self.inorderTraversalHelper(root.right,res)





            


s = Solution()

a3 = TreeNode(3)

a2 = TreeNode(2,a3)

a1 = TreeNode(1,None,a2)

f = s.inorderTraversal(a1)
print(f)

# 
 