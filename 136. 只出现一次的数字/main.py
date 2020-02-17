class Solution:
    def singleNumber(self, nums) -> int:

        numsDict = {}
        for i in range(len(nums)):
            if numsDict.get(nums[i])==None:
                numsDict[nums[i]] = 1
            else:
                numsDict.pop(nums[i])
     
        return numsDict.popitem()[0]

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

        
        
s = Solution()


res = s.singleNumber([4,1,2,1,2])


print(res)
