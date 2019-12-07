

class Solution:
	def twoSum(self, nums,  target) :
		res = []
		# 构造map
		numsDict = {}
		for i in range(len(nums)):
			if numsDict.get(nums[i])==None:
				numsDict[nums[i]] = i
		
		for i in range(len(nums)):
			first = nums[i]
			second = target - first
			index = numsDict.get(second)
			if index!=None and index !=i:
				res.append(i)
				res.append(index)
				return res

		return []
				
			




s = Solution()

print(s.twoSum([1,3,4,5,2,4],6))
