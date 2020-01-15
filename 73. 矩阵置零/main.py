class Solution:
    
    def setZeroes(self, matrix) -> None:
        
        height = len(matrix)
        if height==0:
            return 
        width = len(matrix[0])
        a = []
        for i in range(height):
            for j in range(width):
                if matrix[i][j]==0:
                    a.append([i,j])

        for i in range(len(a)):
            for p in range(0,height):
                matrix[p][a[i][1]] = 0
            for q  in range(0,width):
                matrix[a[i][0]][q] = 0
            


    def setZeroes2(self, matrix) -> None:
        height = len(matrix)
        if height==0:
            return 
        width = len(matrix[0])
        rows = {}
        column = {}
        for i in range(height):
            for j in range(width):
                if matrix[i][j]==0:
                    if rows.get(i)==None:
                        rows[i] = True
                    if column.get(j)==None:
                        column[j] = True
        for i in rows:
            for j in range(width):
                matrix[i][j] = 0

        for j in column:
            for i in range(height):
                matrix[i][j] = 0

   
        



        
            
            
            

s = Solution()

matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
s.setZeroes2(matrix)
print(matrix)
 