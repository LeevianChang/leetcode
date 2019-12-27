class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        resList = []
        self.getSumList(candidates,target,resList,0,[])
        return resList



    def getSumList(self,candidates,target,resList,index,thisList):
        if target==0:
            resList.append(thisList[:])
            return 
        for i in range(index,len(candidates),1):
            
            if target-candidates[i]<0:
                break
            if target-candidates[i]>=0:
                thisList.append(candidates[i])
                self.getSumList(candidates,target-candidates[i],resList,i,thisList)
                thisList.pop()


        
       
        






        

s = Solution()
f = s.combinationSum([2,3,5],8)
print(f)
