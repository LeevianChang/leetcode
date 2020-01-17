class Solution:
    def removeDuplicates(self, nums) -> int:
        length = len(nums)
        if length==0:
            return 0
        i = j = 1
        needChange = False
        while j<length:
            if nums[j]==nums[j-1]:
                if needChange==False:
                    nums[i] = nums[j]
                    needChange = True
                    i+=1
            else:
                needChange = False
                nums[i] = nums[j]
                i+=1
            j+=1
        return i
            


    

            


s = Solution()

f = s.removeDuplicates([1,1,1,2,2,3])
print(f)
 