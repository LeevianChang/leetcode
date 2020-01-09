
import collections

class Solution:

    def getPermutation(self, n: int, k: int) -> str:
        numsList = list(range(1,n+1))
        s = ""
        k = k-1
        for i in range(n,0,-1):
            fac = self.factorial(n-1)
            res = k//fac
            s = s+str(numsList[res])
            del(numsList[res])
            n = n-1
            k = k%fac
            
        return s
            
            
            
        
    def factorial(self,number):
        res = 1
        for i in range(1,number+1):
            res = res*i
        return res

s = Solution()
f = s.getPermutation(4,9)
print(f)
 