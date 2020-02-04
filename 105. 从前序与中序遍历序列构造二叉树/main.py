class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def buildTree(self, preorder, inorder) -> TreeNode:
        
        if len(preorder)>0:
            root = TreeNode(preorder[0])
            self.buildTreeHelper(preorder[1:],inorder,root)
            return root
        else:
            return None

    def buildTreeHelper(self,preorder,inorder,root):
        if len(inorder)==0:
            return None
        left = []
        right = []
        leftEnd = 0
        for i in range(len(inorder)):
            if inorder[i]!=root.val:
                left.append(inorder[i])
            else:
                leftEnd = i
                break
        right = inorder[leftEnd+1:]
        if len(left)>0:
            root.left = self.buildTreeHelper(preorder[1:len(left)],left,TreeNode(preorder[0]))
        if len(right)>0:
            root.right = self.buildTreeHelper(preorder[len(left)+1:],right,TreeNode(preorder[len(left)]))

        
        return root


        
        


        
s = Solution()



res = s.buildTree([1,2,3],[3,2,1])


print(res.val)
print(res.left.val)
print(res.left.left.val)
# print(res.right.val)
# print(res.right.left.val)
# print(res.right.right.val)

 