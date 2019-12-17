class Solution:
    # 使用分治的思想
    def threeSumClosest(self, nums,target):
        # 排序
        nums.sort()
        diff = float("inf")
        add = 0
        if len(nums)==3:
            return nums[0]+nums[1]+nums[2]
        for mid in range(1,len(nums)-1):
            left = 0
            right = len(nums)-1
            while left<mid and right>mid:
                thisAdd = nums[left]+nums[mid]+nums[right]
                if abs(thisAdd-target)<abs(diff):
                    diff = thisAdd-target
                    add = thisAdd
                    if diff==0:
                        return thisAdd
                if thisAdd>target:
                    right-=1
                    continue
                if thisAdd<target:
                    left+=1
                    continue
        return add




s = Solution()

f = s.threeSumClosest([1,2,4,8,16,32,64,128],82)

print(f)