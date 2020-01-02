class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if (len(nums1)+len(nums2))%2 ==0:
            mid_left = int((len(nums1)+len(nums2))/2)
            mid_right = int((len(nums1)+len(nums2))/2)+1
        
            left = self.findMidNumber(mid_left,0,nums1,nums2)
            right = self.findMidNumber(mid_right,0,nums1,nums2)
          
            return (left+right)/2
        else:
            mid = int((len(nums1)+len(nums2))/2)+1

            return self.findMidNumber(mid,0,nums1,nums2)
    
    # 二分法,使用递归的方法找出mid的内容，hasGot用来记录已经去掉的个数
    def findMidNumber(self,mid,hasGot,nums1,nums2):
        k = int((mid-hasGot)/2)
        # print(nums1,nums2,k,mid)
        if k==0:
            if len(nums1)>0 and len(nums2) >0:
                if nums1[0]<nums2[0]:
                    return nums1[0]
                else:
                    return nums2[0]
            elif len(nums1)==0:
                return nums2[0]
            else :
                return nums1[0]

        
        if len(nums1)>0:
            if len(nums1)<=k:
                last_nums1 =len(nums1)-1
            else:
                last_nums1 =  k-1
        if len(nums2)>0:
            if len(nums2)<=k:
                last_nums2 = len(nums2)-1
            else:
                last_nums2 = k-1
        if len(nums1)>0 and len(nums2)>0:
            if nums1[last_nums1]<nums2[last_nums2]:
                return self.findMidNumber(mid,hasGot+len(nums1[:last_nums1+1]),nums1[last_nums1+1:],nums2)
            else:
                return self.findMidNumber(mid,hasGot+len(nums2[:last_nums2+1]),nums1,nums2[last_nums2+1:])
        elif len(nums1)==0:
            return self.findMidNumber(mid,hasGot+len(nums2[:last_nums2+1]),nums1,nums2[last_nums2+1:])
        elif len(nums2)==0:
            return self.findMidNumber(mid,hasGot+len(nums1[:last_nums1+1]),nums1[last_nums1+1:],nums2)

    def findMedianSortedArrays2(self, nums1, nums2):
        length1 = len(nums1)
        length2 = len(nums2)

        length = length1+length2

        if length%2 == 0:
            left = self.findNnumber(nums1,nums2,int(length/2))
            right = self.findNnumber(nums1,nums2,int(length/2+1))
        else:
            left = right = self.findNnumber(nums1,nums2,int(length/2)+1)

        return (left+right)/2

    def findNnumber(self,nums1,nums2,n):
        if n==1:
            if len(nums1)>0 and len(nums2)>0:
                print( min(nums1[0],nums2[0]))
                return min(nums1[0],nums2[0])
            elif len(nums1)>0:
                return nums1[0]
            else:
                return nums2[0]

        
        if len(nums1)==0:
            return nums2[n-1]
        if len(nums2)==0:
            return nums1[n-1]
        k = int(n/2)
        if k-1>=0 and k<len(nums1):
            nums1Last = nums1[k-1]
        elif k-1==0 and k<len(nums1):
            nums1Last = nums1[0]

        else:
            nums1Last = nums1[-1]
            k = len(nums1)
        if k-1>=0 and k<len(nums2):
            nums2Last = nums2[k-1]
        else:
            k = len(nums2)
            nums2Last = nums2[-1]

        if nums1Last<nums2Last:
           return self.findNnumber(nums1[k:],nums2,n-k)
        else:
           return self.findNnumber(nums1,nums2[k:],n-k)

    



s = Solution()

f = s.findMedianSortedArrays([],[2,3])

print(f)