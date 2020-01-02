class Solution:
    maxCount = 0
    def permute(self, nums):
        resList = []
        # for i in range(len(nums)):
        self.permuteRecursion(nums,len(nums),resList,[])
        return resList
    def permuteRecursion(self,nums,length,resList,currList):    
        if len(currList)==length:
            resList.append(currList[:])
            return
        
        for i in range(len(nums)):
            currList.append(nums[i])
            # 把当前遍历的值去除，再递归
            self.permuteRecursion(nums[:i]+nums[i+1:],length,resList,currList)
            currList.pop()
         
        


            
s = Solution()
f = s.permute([1,2,3])
print(f)
