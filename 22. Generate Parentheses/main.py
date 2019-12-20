class Solution:
    def generateParenthesis(self, n):
        resList = []
        self.generate(0,0,n,"",resList)
        return resList
        
    def generate(self,beginTimes,endTimes,n,temp,resList):
        
        if len(temp)==n*2:
            resList.append(temp)
        if beginTimes<n:
            self.generate(beginTimes+1,endTimes,n,temp+"(",resList)
        if endTimes<beginTimes:
            self.generate(beginTimes,endTimes+1,n,temp+")",resList)

            
        
            
s = Solution()

f = s.generateParenthesis(3)

print(f)