class Solution:

    def minimumTotal(self, triangle) -> int:
        if len(triangle)==0:
            return triangle[0]
        batch = []
        batch = triangle[0] 
        for i in range(1,len(triangle)):
            batch = [0]+batch+[0]
            current = []    

            for j in range(len(triangle[i])):
                num1 = triangle[i][j]+batch[j]
                num2 = triangle[i][j]+batch[j+1]
                if j!=0 and j!=len(triangle[i])-1:
                    current.append(min(num1,num2))
                else:

                    current.append(num1)
                    current.append(num2)
            batch = current[1:-1]
  
        return min(batch)
                



        

        



        
        
s = Solution()



res = s.minimumTotal([
    [2],
    [3,4],
    [6,5,9],
    [4,4,8,0]
    ])
print(res)

 