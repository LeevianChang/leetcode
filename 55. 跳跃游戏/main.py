
import copy
class Solution:
    def canJump(self, nums):
        if 0 not in nums:
            return True
        # k 为可以跳的最远距离
        k = 0
        for i in range(len(nums)):
            # 如果已经遍历到无法跳跃的距离，返回False
            if i>k:
                return False
            k = max(k,i+nums[i])

        return True

            

    def canJump2(self,nums):
        return self.futherJump(nums,0)

    def futherJump(self,nums,index):
        if index==len(nums)-1:
            return True
        jump = min(nums[index]+index,len(nums)-1)
        for i in range(index,jump):
            if self.futherJump(nums,i+1):
                return True

        return False


    def canJump3(self, nums):
        if 0 not in nums:
            return True
        # 只要0 不是必经之路，就有解
        return self.cross(nums,0,nums[0])

    def cross(self,nums,index,remain):
        
        if index==len(nums)-1:
            return True
        long = min(index+remain,len(nums))
        for i in range(index,long):
            if i==len(nums)-1:
                return True
                 
            if self.cross(nums,i+1,nums[i+1]):
                return True

        return False

            

        
s = Solution()
f = s.canJump2( [3,2,1,0,4])
print(f)
