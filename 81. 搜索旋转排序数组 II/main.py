class Solution:
    def search(self, nums, target: int) -> bool:
        i = 0
        j = len(nums)-1
        if j==-1:
            return False
        return self.searchHelper(nums,i,j,target)

    def searchHelper(self,nums,i,j,target):
        if i==j:
            return nums[i]==target
        if nums[i]==target or nums[j]==target:
           
            return True

        mid = int(i+(j-i)/2)
        if nums[i]<nums[mid]:
            if target>nums[i] and target<=nums[mid]:
                if self.searchHelper(nums,i,mid,target):
                    return True
        else:
            if self.searchHelper(nums,i,mid,target):
                return True
        if nums[mid+1]<nums[j]:
            if target>=nums[mid+1] and target<nums[j]:
                if self.searchHelper(nums,mid+1,j,target):
                    return True
        else:
            if self.searchHelper(nums,mid+1,j,target):
                return True
        return False
        







    


s = Solution()

f = s.search([5,1,3],1)
print(f)
 