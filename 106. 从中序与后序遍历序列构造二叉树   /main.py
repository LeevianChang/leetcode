class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def buildTree(self, inorder,postorder) -> TreeNode:
        
        if len(postorder)>0:
            root = TreeNode(postorder[-1])
            self.buildTreeHelper(inorder,postorder[:-1],root)
            return root
        else:
            return None

    def buildTreeHelper(self,inorder,postorder,root):
        if len(inorder)==0:
            return None
        left = []
        right = []
        rightEnd = -1
        for i in range(len(inorder)-1,-1,-1):
            if inorder[i]!=root.val:
                right.insert(0,inorder[i])
            else:
                rightEnd = i
                break
        left = inorder[:rightEnd]
        
        if len(left)>0:
            root.left = self.buildTreeHelper(left,postorder[:len(left)-1],TreeNode(postorder[len(left)-1]))
        if len(right)>0:
            # print(postorder)
   
            root.right = self.buildTreeHelper(right,postorder[len(left):-1],TreeNode(postorder[-1]))

        
        return root


        
        


        
s = Solution()



res = s.buildTree([9,3,15,20,7],[9,15,7,20,3])


print(res.val)
print(res.left.val)
# print(res.left.val)
# print(res.left.right.val)
print(res.right.val)
print(res.right.left.val)
print(res.right.right.val)

 