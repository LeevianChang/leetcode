class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def levelOrderBottom(self, root: TreeNode):
        resList = []
        queue = []
        if root!=None:
            queue.append([root,1])
            current = [root.val]
            last = 0
            while len(queue)>0:

                head = queue.pop(0)
                if head[1]>last:
                    resList.insert(0,current[:])
                    current = []
                last = head[1]
                if head[0].left!=None:
                    queue.append([head[0].left,last+1])
                    current.append(head[0].left.val)
                if head[0].right!=None:
                    queue.append([head[0].right,last+1])
                    current.append(head[0].right.val)
                

        return resList


        
s = Solution()
p1left =  TreeNode(15)
p1right =  TreeNode(7)
pLeft = TreeNode(20,p1left,p1right)
pRight = TreeNode(9)
p = TreeNode(3,pLeft,pRight)

res = s.levelOrderBottom(p)


print(res)

 