class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        self.flattenHelper(root)
        return root



    def flattenHelper(self,root):
        head = root
        while root!=None:
            if root.left==None:
                root = root.right
                continue
            rootRight = root.right
            rootLeft = root.left

            while rootLeft.right!=None:
                rootLeft = rootLeft.right
            rootLeft.right = rootRight
            root.right = root.left
            root.left = None
                
            root = root.right
        return head
        



        
        
        

rootLeft = TreeNode(2,TreeNode(3),TreeNode(4))
rootRight = TreeNode(5,None,TreeNode(6))
root = TreeNode(1,rootLeft,rootRight)
        
s = Solution()



res = s.flatten(root)
print(res.val)
print(res.right.val)
print(res.right.right.val)
print(res.right.right.right.val)
print(res.right.right.right.right.val)


 