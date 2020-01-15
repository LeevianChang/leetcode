import math
class Solution:
    
    def simplifyPath(self, path: str) -> str:
        res = "/"
        l = path.split("/")
        stack = []
        for i in range(len(l)):
            if l[i]=="" or l[i]==".":
                continue
            if l[i]!="..":
                stack.append(l[i])
            else:
                if len(stack)>=1:
                    stack.pop()
        
        res +="/".join(stack)
        return res
        
        
    

s = Solution()
f = s.simplifyPath("/a//b////c/d//././/..")
print(f)
 