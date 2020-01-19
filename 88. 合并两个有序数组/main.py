class Solution:
    
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        i = 0
        j = 0
        while i<len(nums1) and j<n:
            if i>=m:
                nums1[i]=nums2[j]
                i+=1
                j+=1
                continue
            if nums1[i]<=nums2[j]:
                i+=1
                continue
            temp = nums1[i]
            nums1[i] = nums2[j]
            nums2[j]=temp
            nums2.sort()
            
        

s = Solution()

nums1 = [4,5,6,0,0,0]
s.merge(nums1,3,[1,2,3],3)


print(nums1)

 