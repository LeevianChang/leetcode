class Solution:
    start = -1
    end = -1
    def searchRange(self, nums, target):
        self.start = len(nums)
        self.end = -1
        if len(nums)>0:
            self.search(nums,target,0,len(nums)-1)
        if self.start==len(nums):
            return [-1,-1]
        else:
            return [self.start,self.end]


    def search(self,nums,target,i,j):
        if i==j:
            if target==nums[i]:
                if i<self.start:
                    self.start = i
                if i>self.end:
                    self.end = i
                return 
            else:
                return 
        
        mid = int((i+j)/2)
        if nums[mid]>=target:
            self.search(nums,target,i,mid)
        if nums[mid+1]<=target:
            self.search(nums,target,mid+1,j)


        
                

        
        



    

    

s = Solution()
f = s.searchRange([1],1)
print(f)
