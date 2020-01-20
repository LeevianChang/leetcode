class Solution:
   


    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        self.subsetsWithDupHelper(n,nums,0,[],res)
        return res


    def subsetsWithDupHelper(self,n,nums,index,current,res):
        if current not in res:
            res.append(current)
        for i in range(index,n):
            
            self.subsetsWithDupHelper(n,nums,i+1,current+[nums[i]],res)
            

s = Solution()

f = s.subsetsWithDup([1,2,2])
print(f)
 