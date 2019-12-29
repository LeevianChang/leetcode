class Solution:
    def firstMissingPositive(self, nums):
        self.preOperation(nums)
        resList = [0]*(len(nums)+1)
        for i in range(len(nums)):
            if nums[i]>0:
                resList[nums[i]] = 1

        res = len(nums)+1

        for i in range(1,len(resList),1):
            if resList[i]==0:
                res = i
                break
        return res
        



    # 预操作
    def preOperation(self,nums):
        maxNum = len(nums)+1
        for i in range(len(nums)):
            if nums[i]<0 or nums[i]>=maxNum:
                nums[i] = 0 
            

        

s = Solution()
f = s.firstMissingPositive([2])
print(f)
