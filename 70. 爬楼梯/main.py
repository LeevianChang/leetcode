import math
class Solution:
    
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        first = 1
        second = 2
        for _ in range(3, n+1):
            temp = first+second
            first = second
            second =temp
        return second


        
        

        

        



    

s = Solution()
f = s.climbStairs(3)
print(f)
 