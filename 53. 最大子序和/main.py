
import copy
class Solution:
    def maxSubArray(self, nums):
        maxRes = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
            maxRes = max(maxRes,nums[i])

        return maxRes

    # 二分法
    def maxSubArray2(self, nums):
        return self.getMaxSum(nums,0,len(nums)-1)

    def getMaxSum(self,nums,left,right):
        if left==right:
            return nums[left]
        mid = int((right+left)/2)
        leftSum = self.getMaxSum(nums,left,mid)
        rightSum =self.getMaxSum(nums,mid+1,right)
       
        crossSum = self.getMaxCrossRes(nums,left,mid,right)
        return max(leftSum,rightSum,crossSum)
        
    def getMaxCrossRes(self,nums,left,mid,right):
        maxLeft = nums[mid]
        leftSum = nums[mid]
        for i in range(mid-1,left-1,-1):
            leftSum += nums[i]
            maxLeft = max(maxLeft,leftSum)
        maxRight = nums[mid+1]
        rightSum = nums[mid+1]
        
        for i in range(mid+2,right+1):
            rightSum += nums[i]
            maxRight = max(maxRight,rightSum)
        return (maxLeft+maxRight)

        

        
s = Solution()
f = s.maxSubArray2([-1,9999,-1])
print(f)
