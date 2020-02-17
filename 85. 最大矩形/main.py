class Solution:
   


    def maximalRectangle(self, matrix) -> int:
        maxArea = 0
        for i in range(len(matrix)):
            heights = []
            for j in range(len(matrix[i])):
                # print(matrix[i][j])
                if matrix[i][j]!="0":
                    k = i
                    h = 0
                    while k>=0:
                        if matrix[k][j]=="1":
                            h = h+1
                            k-=1
                        else:
                            break
                    heights.append(h)
                else:
                    heights.append(0)
            maxArea = max(maxArea,self.maxAreaResult(heights))

        return maxArea     


    def maxAreaResult(self,heights):
        maxArea = 0
        stack = []
        heights = [0]+heights+[0]

        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                top = stack.pop()
                maxArea = max(maxArea,heights[top]*(i-1-stack[-1]))
            stack.append(i)

        return maxArea







    


s = Solution()
a = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

f = s.maximalRectangle(a)
print(f)
 