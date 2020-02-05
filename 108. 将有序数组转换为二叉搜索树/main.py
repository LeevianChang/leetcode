class TreeNode:
    def __init__(self, x,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
class Solution:
    

    def sortedArrayToBST(self, nums) -> TreeNode:
        return self.sortedArrayToBSTHelper(nums)
      
    def sortedArrayToBSTHelper(self,nums):
        if len(nums)==0:
            return None
        mid = int(len(nums)/2)
        root = TreeNode(nums[mid])
        
        root.left = self.sortedArrayToBSTHelper(nums[0:mid])
        
        root.right = self.sortedArrayToBSTHelper(nums[mid+1:])

        return root


        


        
s = Solution()



res = s.sortedArrayToBST([-10,-3,0])


print(res.val)
print(res.left.val)
# print(res.left.right.val)
# print(res.left.val)
# print(res.left.right.val)
print(res.right.val)
# print(res.right.left.val)
# print(res.right.right.val)

 