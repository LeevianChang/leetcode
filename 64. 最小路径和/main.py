

class Solution:



    def minPathSum(self, grid):
        # n行 m列
        n = len(grid)
        if n==0:
            return 1
        m = len(grid[0])
        a = [0]*m
        a = []
        for _ in range(n):
            a.append([0]*m)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i==0:
                    if j==0:
                        a[i][j]=grid[i][j]
                    else:
                        a[i][j] = grid[i][j]+a[i][j-1]
                    continue
                if j==0:
                    a[i][j] = grid[i][j]+a[i-1][j]
                    continue
                a[i][j] = min(a[i-1][j],a[i][j-1])+grid[i][j]
        # print(a)
        return a[n-1][m-1]

    def minPathSum2(self, grid):
        # n行 m列
        n = len(grid)
        if n==0:
            return 1
        m = len(grid[0])
        
        a = [0]*m
 
        lastM = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i==0:
                    if j==0:
                        a[j] = grid[i][j]
                        lastM = a[j]
                    else:
                        a[j] = lastM+grid[i][j]
                        lastM = a[j]
                    
                    continue
                if j==0:
                    a[j] = a[j]+grid[i][j]
                    lastM = a[j]
                else:
                    a[j] = min(lastM,a[j])+grid[i][j]
                    lastM = a[j]
                
        return a[m-1]

                
        
                

s = Solution()
grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
f = s.minPathSum2(grid)
print(f)
 