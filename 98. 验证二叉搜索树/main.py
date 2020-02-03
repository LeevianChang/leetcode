class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidBSTHelper(root,float('-inf'),float('inf'))

    def isValidBSTHelper(self, root: TreeNode,lower,higher):
        if root==None:
            return True
        val = root.val
        if val<=lower or val>=higher:
            return False
        
        l1 =  self.isValidBSTHelper(root.left,lower,val)
        l2 =  self.isValidBSTHelper(root.right,val,higher)

        return l1 and l2



            


s = Solution()

a5 = TreeNode(6)

a4 = TreeNode(3)

a3 = TreeNode(4,a4,a5)

a2 = TreeNode(1)

a1 = TreeNode(5,a2,a3)

# a3 = TreeNode(3)

# a2 = TreeNode(1)

# a1 = TreeNode(2,a2,a3)


# a5 = TreeNode(20)

# a4 = TreeNode(6)

# a3 = TreeNode(15,a4,a5)

# a2 = TreeNode(5)
# a1 = TreeNode(10,a2,a3)



f = s.isValidBST(a1)
print(f)

# 
 