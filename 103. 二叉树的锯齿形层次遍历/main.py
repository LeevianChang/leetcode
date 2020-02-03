class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def zigzagLevelOrder(self, root: TreeNode):
        resList = []
        queue = []
        if root!=None:
            queue.append([root,1])
            current = [root.val]
            last = 0
            while len(queue)>0:

                head = queue.pop(0)
                if head[1]>last:
                    resList.append(current[:])
                    current = []
                last = head[1]
                if head[0].left!=None:
                    queue.append([head[0].left,last+1])
    
                    self.insertCurrent(current,head[0].left,last)

                if head[0].right!=None:
                    queue.append([head[0].right,last+1])
                    self.insertCurrent(current,head[0].right,last)

        return resList

    
    def insertCurrent(self,current,root,last):
        if last%2==1:
            current.insert(0,root.val)
        else:
            current.append(root.val)



        
s = Solution()

p1right =  TreeNode(5)
pRight = TreeNode(3,None,p1right)
pleft1 = TreeNode(4)
pLeft = TreeNode(2,pleft1)
p = TreeNode(1,pLeft,pRight)

res = s.zigzagLevelOrder(p)


print(res)

 