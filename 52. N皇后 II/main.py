
import copy
class Solution:
    def totalNQueens(self, n):
        res = [0]
        
        cantChose = {"add":[],"minus":[]}

       
        self.choseNQueens(n,0,0,[],cantChose,[],res)
        return res[0]

    def choseNQueens(self,n,i,j,columned,cantChose,currentList,res):
        
        if i==n:        
            res[0]+=1
            return 
            
        isChose = False
        for j in range(0,n):
            if j in columned:
                continue
            if  i+j in cantChose["add"] or i-j in cantChose["minus"]:
                continue
            
            queenRows = ""
            
            queenRows = "."*j+"Q"+"."*(n-j-1)
            currentList.append(queenRows)
            columned.append(j)
            isChose = True
            # 对列表进行深拷贝
            newCantChose = copy.deepcopy(cantChose)
            newCantChose["add"].append(i+j)
            newCantChose["minus"].append(i-j)
                   
           
            self.choseNQueens(n,i+1,0,columned,newCantChose,currentList,res)
            currentList.pop()
            columned.pop()
        if isChose==False:
            return 
    

          



        





          


            
s = Solution()
f = s.totalNQueens(5)
print(f)
