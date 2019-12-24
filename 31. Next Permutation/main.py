class Solution:
    def nextPermutation(self, nums):
        last = nums[len(nums)-1]
        first = len(nums)
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>=last:
                last = nums[i]
                continue
            else:
                first = i
                break
        if first!=len(nums):
            for j in range(len(nums)-1,first,-1):
                print(len(nums))
                if nums[j]>nums[first]:
                    self.swap(first,j,nums)
                    break
        else:
            first = -1
        for j in range(1,int((len(nums)-first)/2)+1):
            self.swap(first+j,len(nums)-j,nums)
            


    def swap(self,i,j,nums):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


    

    

s = Solution()
numsList = [3,2,1]
s.nextPermutation(numsList)
print(numsList)
