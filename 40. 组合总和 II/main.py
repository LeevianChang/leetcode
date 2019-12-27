class Solution:
   
    def combinationSum2(self, candidates, target):
        resList = []
        candidates.sort()
        self.GetSumList(candidates,target,resList,0,[])

        return resList


    def GetSumList(self,candidates,target,resList,index,thisList):
        if index>len(candidates):
            return 
        if target==0:
            resList.append(thisList[:])
            return 
        for i in range(index,len(candidates),1):
            # 不能重复
            if i>index and candidates[i]==candidates[i-1]:
                continue
            if target-candidates[i]>=0:
            
                thisList.append(candidates[i])
                self.GetSumList(candidates,target-candidates[i],resList,i+1,thisList)
                thisList.pop()
            if target-candidates[i]<0:
                return 

        






        

s = Solution()
f = s.combinationSum2([1,2,2,2,5],5)
print(f)
