class Solution:

    def getRow(self, rowIndex: int):

        init = [0,1,0] 

        for i in range(rowIndex):
            for j in range(len(init)-1):
                init[j] = init[j]+init[j+1]
            init = [0]+init[:-1]+[0]


        return init[1:-1]


        

        

        



        
        
s = Solution()



res = s.getRow(0)
print(res)

 