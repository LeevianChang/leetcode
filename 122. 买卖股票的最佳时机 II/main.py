class Solution:

    def maxProfit(self, prices) -> int:
        stack = []
        maxRes = 0 
        for i in range(len(prices)):
            if len(stack)==0:
                stack.append(prices[i])

                continue
            if prices[i]<stack[-1]:
                if len(stack)==1:
                    stack.pop()
                    stack.append(prices[i])
                    continue
                maxRes += stack[-1]-stack[0]
                stack = [prices[i]]
                continue
            stack.append(prices[i])

        if len(stack)>1:
            maxRes +=stack[-1]-stack[0]
        return maxRes

            




        
        
s = Solution()



res = s.maxProfit([])
print(res)

 