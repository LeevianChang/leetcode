import math
class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        a = []
        for i in range(n+1):
            a.append([0]*(m+1))
        for i in range(n+1):
            for j in range(m+1):
                if i==0:
                    a[i][j] = j
                    continue
                if j==0:
                    a[i][j] = i
                    continue
                if word1[i-1]==word2[j-1]:
                    a[i][j] = a[i-1][j-1]
                else:
                    a[i][j] = min(a[i-1][j-1],a[i-1][j],a[i][j-1])+1
        return a[n][m]

        
        
    

s = Solution()
f = s.minDistance("intention","execution")
print(f)
 