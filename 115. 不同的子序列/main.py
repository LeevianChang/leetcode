class Solution:
   
    count = 0

    def numDistinct(self, s: str, t: str) -> int:

        self.numDistinctHelper(s,t)
        return self.count
        
    def numDistinctHelper(self,s,t):
        if len(t)==0:
            self.count+=1
            return
        
        
        if t[0] in s and len(s)>=len(t):
            for j in range(len(s)):
                if s[j]==t[0]:
                    self.numDistinctHelper(s[j+1:],t[1:])
        else:
            return 


    def numDistinct2(self,s,t):

        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]

        for i in range(len(s)+1):
            dp[0][i] = 1
        for i in range(1,len(t)+1):
            for j in range(1,len(s)+1):
                
                if t[i-1]==s[j-1]:
                    dp[i][j] =  dp[i-1][j-1]+dp[i][j-1]
                else:
                    dp[i][j] =  dp[i][j-1]




        print(dp)
        return dp[-1][-1]

                



       
    



s = Solution()

f = s.numDistinct2("rabbbit",
"rabbit")
print(f)
 