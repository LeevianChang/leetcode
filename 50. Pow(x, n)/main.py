class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n==1:
            return x
        if n==-1:
            return 1/x
        if n%2==1:
            even = n-1
        else:
            even = n
        if even==n:
            return self.myPowHelper(x,even)
        else:
            
            return self.myPowHelper(x,even)*x
        
        

    def myPowHelper(self,x,n):
        if n==1:
            return x
        if n==-1:
            return 1/x
        if n%2==1:
            a = self.myPowHelper(x,(n-1)/2)
            return a*a*self.myPowHelper(x,1)
        else:
            a = self.myPowHelper(x,n/2)
            return a*a

        



            
s = Solution()
f = s.myPow(8.84372, -5)
print(f)
