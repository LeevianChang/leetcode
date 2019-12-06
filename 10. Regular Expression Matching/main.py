class Solution:
    # 使用递归的方式
    def isMatch(self, s: str, p: str) -> bool:
        if not p :
            return not s
        
        headMatch = False
        if len(s)>0:
            if p[0]=='.':
                headMatch = True
            elif p[0]==s[0]:
                headMatch = True
        
        if len(p)>1 and p[1]=="*":
            if headMatch:
                # 需要考虑两种情况，分别做递归
                return  self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
            else:
                return self.isMatch(s,p[2:])
        else:
            return headMatch and self.isMatch(s[1:],p[1:])