class Solution:
    def permuteUnique(self, nums):
        resList = []
        # for i in range(len(nums)):
        nums.sort()
        self.permuteRecursion(nums,len(nums),resList,[])
        return resList
    def permuteRecursion(self,nums,length,resList,currList):    
        if len(currList)==length:
            resList.append(currList[:])
            return
        
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            currList.append(nums[i])
            # 把当前遍历的值去除，再递归
            self.permuteRecursion(nums[:i]+nums[i+1:],length,resList,currList)
            currList.pop()
        


            
s = Solution()
f = s.permuteUnique([1,1,2])
print(f)
