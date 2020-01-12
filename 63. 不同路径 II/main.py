

class Solution:



    def uniquePathsWithObstacles(self, obstacleGrid) :
        n = len(obstacleGrid)
        if n==0:
            return 1
        m = len(obstacleGrid[0])
        a = [0]*m
        a = []
        for _ in range(n):
            a.append([0]*m)
        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j]==0:

                    if i==0:
                        if j>0:
                            if  obstacleGrid[i][j]==1 or a[i][j-1]==0:
                                a[i][j]=0
                            else:
                                a[i][j]=1
                        else:
                            a[i][j]=1
                        continue

                    if j==0:
                        if i>0:
                            if  obstacleGrid[i][j]==1 or a[i-1][j]==0:
                                a[i][j]=0
                            else:
                                a[i][j]=1
                        else:
                            a[i][j]=1
                        continue
                        
                    a[i][j] = a[i-1][j]+a[i][j-1]
                            
                else:
                    a[i][j]=0



                
        return a[n-1][m-1]
                

s = Solution()
obstacleGrid = [
    # [0,0,0,0],
    # [0,1,0,0],
    # [0,0,0,0],
    # [0,0,1,0],
    # [0,0,0,0]
    # [1,0]
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
f = s.uniquePathsWithObstacles(obstacleGrid)
print(f)
 