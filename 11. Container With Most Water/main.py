class Solution:
    def maxArea(self, height):
        i = 0 
        j = len(height)-1
        maxAreaValue = 0
    
        while i!=j:
            minHeight = height[i]
            
            if minHeight>height[j]:
                minHeight = height[j]
                j = j-1
            else:
                i = i+1
            area =  minHeight*(j-i+1)
            if area>maxAreaValue:
                maxAreaValue = area
        return maxAreaValue






s = Solution()

f = s.maxArea([1,8,6,2,5,4,8,3,7])

print(f)