class Solution:
    maxCount = 0
    def jumpDp(self, nums):
        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0
        # i 为从第1个到最后一个的index
        for i in range(1, len(nums)):
            # index 是比i小的索引
            for j in range(i):
                # 计算比从j到i的距离是否是当前的nums[j]可抵达的，如果可以跳过去，则和当前的比较，选择较小的那个
                if nums[j] >= i - j:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]

    def jump(self, nums):
        n = len(nums)
        dp = [0]*n
        if n==1:
            return 0
        for i in range(n):
            for j in range(nums[i],0,-1):
                if i+j>=n-1:
                    return dp[i]+1
                elif dp[i+j]==0:
                    dp[i+j] = dp[i]+1
                else:
                    break


    def jump2(self, nums):
        maxPosition = 0
        end = 0
        count = 0
        for i in range(len(nums)-1):
            maxPosition = max(maxPosition,i+nums[i])
            if i==end:
                end = maxPosition
                count+=1
        return count

                

        
                
                




            
s = Solution()
f = s.jump2([2,3,1,1,4])
print(f)
