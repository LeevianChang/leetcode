class Solution:
    def isMatch(self, s, p):
        i = 0
        j = 0
        start = -1
        lastI = 0

        while i <len(s):
            if j<len(p) and (p[j]==s[i] or p[j]=="?"):
                i+=1
                j+=1
            #当前是星号，start记录星号的位置，lastI记录本次i的位置
            elif j<len(p) and p[j]=="*":
                start = j
                lastI = i
                j = j+1
            elif start!=-1:
                # 移动到星号后面的位置
                j = start+1
                lastI+=1
                #移动到上次的位置后
                i = lastI
            else:
                return False
        for i in range(j,len(p)):
            if p[i]=="*":
                continue
            else:
                return False
        
        return True

    def isMatchDp(self, s, p):
        # dp初始化,dp是一个二位数组，dp[i][j]表明s[i-1]和p[j-1]是否匹配
        dp = []
        sn = len(s)
        pn = len(p)
        for _ in range(sn+1):
            dp.append([False]*(pn+1))
        dp[0][0] = True

        for j in range(1,pn+1):
            if p[j-1]=="*":
                
                dp[0][j] =dp[0][j-1] 


        for i in range(1,sn+1):
            for j in range(1,pn+1): 
                if p[j-1]==s[i-1] or p[j-1]=="?":
                    dp[i][j] =dp[i-1][j-1]
                elif p[j-1]=="*":
                    # dp[i][j-1] *匹配的是空串的情况
                    # dp[i-1][j] *匹配的是非空串的情况
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

                
        return dp[-1][-1]

            

            
s = Solution()
f = s.isMatch("abba","*bc")
print(f)
