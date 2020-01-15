class Solution:
    
    def searchMatrix(self, matrix, target) -> bool:
        rowsLength = len(matrix)
        if rowsLength==0:
            return False
        columnLength = len(matrix[0])
        if columnLength==0:
            return False
        for i in range(rowsLength):
            if matrix[i][0]<=target and target<=matrix[i][columnLength-1]:
                for j in range(columnLength):
                    if matrix[i][j]==target:
                        return True
                return False
            if matrix[i][0]<=target and matrix[i][columnLength-1]<=target:
                continue
            if matrix[i][0]>target:
                return False
        return False
    

s = Solution()
matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
[]
]
f = s.searchMatrix(matrix,13)
print(f)
 