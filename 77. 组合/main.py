class Solution:
    
    def combine(self, n: int, k: int):
        resList = []
        numberList = list(range(1,n+1))
        self.combineHelper(numberList,k,resList,[])
        return resList

    def combineHelper(self,numberList,k,resList,current):
        # print(numberList)
        if len(current)==k:
            resList.append(current[:])
        for i in range(len(numberList)):
            current.append(numberList[i])
            self.combineHelper(numberList[i+1:],k,resList,current)
            current.pop()
    

s = Solution()
f = s.combine(4,2)
print(f)
 