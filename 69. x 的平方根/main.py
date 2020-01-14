import math
class Solution:

    def mySqrt(self, x: int) -> int:
        left = 0
        right = int(x/2)+1
        while left<right:
            mid = int((left+right)/2+1)
            if mid*mid>x:
                right = mid-1
            else:
                left = mid

        return left



     
       






            





s = Solution()
print(int(math.sqrt( 1234640391 )))
f = s.mySqrt(1234640391)
print(f)
 