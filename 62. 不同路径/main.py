

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 1
        a = []
        
        for _ in range(n):
            a.append([0]*m)
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    a[i][j]=1
                    continue
                a[i][j] = a[i-1][j]+a[i][j-1]
        return a[n-1][m-1]


    def uniquePaths2(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 1
        a = [1]*m
        lastM = 1
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    lastM = 1
                else:
                    lastM = lastM+a[j]
                    a[j] = lastM
        return a[m-1]
                

s = Solution()
f = s.uniquePaths2(7,3)
print(f)
 