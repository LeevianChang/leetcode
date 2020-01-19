class Solution:
   


    def largestRectangleArea(self, heights) -> int:
        stack = []
        # 左右两边增加高度为0的矩阵，作为边界
        heights = [0]+heights+[0]
        maxArea = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                top = stack.pop()
                maxArea = max(maxArea,heights[top]*(i-1-stack[-1]))
            stack.append(i)

        return maxArea




    


s = Solution()

f = s.largestRectangleArea([2,1,5,6,2,3])
print(f)
 