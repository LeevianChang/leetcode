class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:
            return s
        res = ["" for _ in range(numRows)]
        i ,flag = 0,-1
        for c in s:
            res[i]+=c
            if i==0 or i==numRows-1:
                flag = -flag
            i+=flag
            print(i,flag,res)


        return "".join(res)


s = Solution()

f = s.convert("LEETCODEISHIRING",3)

print(f)