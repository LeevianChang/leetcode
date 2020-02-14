class Solution:

    def maxProfit(self, prices) -> int:
        if len(prices)<2:
            return 0
        dp = []*len(prices)
        for i in range(len(prices)):
            dp.append([0]*5)

        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        for i in range(len(prices)):
            dp[i][2] = -float("inf")
            dp[i][3] = -float("inf")
            dp[i][4] = -float("inf")
        for i in range(1,len(prices)):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])
        return max(0, dp[-1][2], dp[-1][4])
        
        
s = Solution()


res = s.maxProfit([3,3,5,0,0,3,1,4])
print(res)

 