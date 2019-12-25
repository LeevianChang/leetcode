class Solution:
    def search(self, nums, target):
        index = -1
        if len(nums)>0:
            t =  self.searchTarget(nums,0,len(nums)-1,target)
        
            if t!=None and  nums[t]==target:
                return t
        return index


    def searchTarget(self,nums,start,end,target):
        if start==end:
            return start
        
        mid = int((start+end)/2)
        
        if target==nums[mid]:
            return mid
        
        
        if target==nums[start]:
            return start
        if target==nums[end]:
            return end
        
        if nums[start]<nums[end]:
            
            if target<nums[mid]:
                return self.searchTarget(nums,start,mid,target)
            else:
                return self.searchTarget(nums,mid+1,end,target)
                

        if nums[start]>nums[end]:
            l = self.searchTarget(nums,start,mid,target)
            r = self.searchTarget(nums,mid+1,end,target)
            if l!=None and nums[l]==target:
                return l
            if r!=None and nums[r]==target:
                return r
            

                
        
        



    

    

s = Solution()
f = s.search([8,1,2,3,4,5,6,7],6)
print(f)
