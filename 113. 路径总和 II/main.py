class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        
        resBath = []
        self.pathSumHelper(root,sum,resBath,[])
        return resBath

    def pathSumHelper(self,root,sum,resBath,current):
        if root==None:
            return 
        sum -=root.val

        if root.left==None and root.right==None:
            if sum==0:
                current.append(root.val)
                resBath.append(current[:])
            return 
    
        self.pathSumHelper(root.left,sum,resBath,current+[root.val]) 

        self.pathSumHelper(root.right,sum,resBath,current+[root.val])

                

rootLeft = TreeNode(4,TreeNode(11,TreeNode(7),TreeNode(2)))
rootRight = TreeNode(8,TreeNode(13),TreeNode(4,TreeNode(5),TreeNode(1)))
root = TreeNode(5,rootLeft,rootRight)
        
s = Solution()



res = s.pathSum(root,22)
print(res)


 