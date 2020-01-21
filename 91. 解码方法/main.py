class Solution:
   


    def numDecodings(self, s: str) -> int:
       
        dpList = [0]*(len(s))
        
        
        for i in range(len(s)-1,-1,-1):
            if s[i]=="0":
                dpList[i] = 0
                continue
            if i==len(s)-1:
                
                if int(s[i]) in range(1,10):
                    dpList[i] = 1
                    continue
            if i==len(s)-2:
                if int(s[i])*10+int(s[i+1])<=26:
                    dpList[i] = dpList[i+1]+1
                else:
                    dpList[i] = dpList[i+1]
                continue
            if int(s[i])*10+int(s[i+1])<=26:
                dpList[i] = dpList[i+1]+dpList[i+2]
            else:
                dpList[i] = dpList[i+1]


        return dpList[0]




s = Solution()

f = s.numDecodings("611")
print(f)
 