class Solution:
    
    def subsets(self, nums):
        resList = []
        self.subsetsHelper(nums,0,resList,[])
        return resList


    def subsetsHelper(self,nums,k,resList,current):
        resList.append(current)
        for i in range(k,len(nums)):
            self.subsetsHelper(nums,i+1,resList,current+[nums[i]])





    

s = Solution()
f = s.subsets([1,2,3,4])
print(f)
 