class Solution:
    def fourSum(self, nums, target):
        resList = []
        if len(nums)<4:
            return resList
        nums.sort()
        length = len(nums)
        # i j k h
        for i in range(length-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            # 找出最大最小值，若不可能满足target值，无需继续判断
            minAdd = nums[i]+nums[i+1]+nums[i+2]+nums[i+3]
            if minAdd >target:
                break
            maxAdd = nums[i]+nums[length-1]+nums[length-2]+nums[length-3]
            if maxAdd<target:
                continue
            for j in range(i+1,length-2):
                

                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                minAdd = nums[i]+nums[j]+nums[j+1]+nums[j+2]
                if minAdd >target:
                    continue
                maxAdd = nums[i]+nums[j]+nums[length-1]+nums[length-2]
                if maxAdd<target:
                    continue
                k = j+1
                h = length -1 
                while k<h:
                    add = nums[i]+nums[j]+nums[k]+nums[h]
                    if add==target:
                        d = []
                        d.append(nums[i])
                        d.append(nums[j])
                        d.append(nums[k])
                        d.append(nums[h])
                        resList.append(d)
                    
                        h-=1
                        # h已经-1，与之前的那个数比较，如果相同，则继续-1
                        while k<h and nums[h]==nums[h+1]:
                            h-=1
                        k+=1
                        while k<h and nums[k]==nums[k-1]:
                            k+=1
                        continue
                    if add>target:
                        h-=1
                        continue
                        
                    if add<target:
                        k+=1
                        continue
        return resList











s = Solution()

f = s.fourSum([-1,0,-5,-2,-2,-4,0,1,-2],-9)

print(f)