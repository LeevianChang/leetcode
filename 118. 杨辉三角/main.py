class Solution:

    def generate(self, numRows: int):
        resBatch = []
        if numRows == 0:
            return resBatch
        resBatch.append([1])
        if numRows  == 1:
            return resBatch
        resBatch.append([1,1])
        if numRows == 2:
            return resBatch
        self.generateHelper(2,numRows,resBatch)
        return resBatch
    
    def generateHelper(self,current,numRows,resBatch):

        
        if current==numRows:
            return resBatch

        c = []
        for i in range(1,current):
            c.append(resBatch[-1][i]+resBatch[-1][i-1])

        resBatch.append([1]+c+[1])

        return self.generateHelper(current+1,numRows,resBatch)



        

        

        



            
        

        
s = Solution()



res = s.generate(2)
print(res)

 