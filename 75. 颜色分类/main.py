class Solution:
    
    def sortColors(self, nums) -> None:
        a = {}
        for i in range(len(nums)):
            if a.get(nums[i])!=None:
                a[nums[i]]+=1
            else:
                a[nums[i]] = 1
        start = 0
        for i in range(3):
            if a.get(i)!=None:
                length = a[i]
                for j in range(start,start+length):
                    nums[j] = i
                start = start+length
           




    

s = Solution()
a = [0]
s.sortColors(a)
print(a)
 