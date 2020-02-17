class Solution:

    def maxProfit(self, prices) -> int:
        maxRes = 0
        for i in range(len(prices)-1):
            maxRemain = max(prices[i+1:])

            if maxRemain-prices[i]>0 and maxRemain-prices[i]>maxRes:
                maxRes = maxRemain-prices[i]


        return maxRes


    def maxProfit2(self,prices):
        if len(prices)==0:
            return 0
        stack = []
        maxRes = 0
        for i in range(len(prices)):
            if len(stack)<1:
                stack.append(prices[i])
                continue
            if prices[i]>stack[-1]:
                stack.append(prices[i])
            
            if prices[i]<=stack[-1] and prices[i]>=stack[0]:
                if len(stack)==1:
                    stack.pop()
                    stack.append(prices[i])
                    continue
            if prices[i]<stack[0]:
                if stack[-1]-stack[0]>maxRes:
                    maxRes = stack[-1]-stack[0]
                
                stack=[]
                stack.append(prices[i])
                
        if stack[-1]-stack[0]>maxRes:
            maxRes = stack[-1]-stack[0]
        return maxRes


    def maxProfit3(self,prices):
        minPrices = float("inf")

        maxDiff = 0

        for i in range(len(prices)):
            if prices[i]<minPrices:
                minPrices = prices[i]
            else:
                if prices[i]-minPrices>maxDiff:
                    maxDiff =prices[i]-minPrices

        return maxDiff         



        
        
s = Solution()



res = s.maxProfit3([4,7,2,1])
print(res)

 