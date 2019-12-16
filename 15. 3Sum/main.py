class Solution:
    def threeSum(self,nums):
        res = []
        if len(nums)<3:
            return res 
        nums.sort()
        # print(nums)
        left = 0
        while left<len(nums)-2:
            if nums[left]>0:
                break
            right = len(nums)-1
            mid = left+1

            while right>left+1:
                if nums[right]<0:
                    break
                
                while mid<right:
                    add = nums[left]+nums[mid]+nums[right]
                    if add==0:
                        d = []
                        d.append(nums[left])
                        d.append(nums[mid])
                        d.append(nums[right])
                        res.append(d)
                        break
                    if add>0:
                        break
                    if add<0:
                        while mid+1<right and  nums[mid]==nums[mid+1]:
                            mid+=1
                        mid+=1
                        
                while right>left+1 and nums[right]==nums[right-1]:
                    right-=1
                right-=1
            while left<len(nums)-2 and nums[left]==nums[left+1]:
                left+=1
            left+=1
        return res






s = Solution()

f = s.threeSum([6,-5,-6,-1,-2,8,-1,4,-10,-8,-10,-2,-4,-1,-8,-2,8,9,-5,-2,-8,-9,-3,-5])

print(f)