class Solution:
    def longestValidParentheses(self, s):
        countList = [0]*len(s)
        maxReturn = 0
        count = 0
        for i in range(len(s)):
            if s[i]=="(":
                continue
            if i>=1 and s[i]==")":
                if s[i-1]=="(":
                    if i>=2:
                        count = countList[i-2]+2

                    else:
                        count = 2
                    countList[i]=count
                    
                if s[i-1]==")":
                    if i>=3:
                        preIndex = i-countList[i-1]-1
                        if preIndex>=0 and s[preIndex]=="(":
                            count = countList[i-1]+2
                            if preIndex-1>0 and s[preIndex-1]==")":
                                count +=countList[preIndex-1]
                            countList[i] = count
                if count>maxReturn:
                    maxReturn = count
                
        return maxReturn



    

    

s = Solution()
f = s.longestValidParentheses("(()())")
print(f)
