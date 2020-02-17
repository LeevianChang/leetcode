class Solution:
   


    def grayCode(self, n: int):
        res = [0]
        for i in range(n):
            for j in range(len(res)-1,-1,-1):
                res.append(res[j]+2**i)

        return res

        



    


s = Solution()

f = s.grayCode(3)
print(f)
 