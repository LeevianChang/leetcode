import re
class Solution:

    def isNumber(self, s: str) -> bool:
        state = 0
        s = s.strip()
        for i in range(len(s)):
            
            if s[i]=="+" or s[i]=="-":
                if state ==0:
                    state = 1
                elif state == 4:
                    state = 6
                else:
                    return False
            elif re.match("[0-9]", s[i])!=None:
                if state>=0 and state<=2:
                    state = 2
                    continue 
                elif state==3:
                    state = 3
                    continue
                elif state>=4 and state<=6:
                    state = 5
                    continue
                elif state==7 or state==8:
                    state = 8
                else:
                    return False
            elif s[i]==".":
                if state==0 or state==1:
                    state = 7
                    continue
                if state==2:
                    state=3
                    continue
                return False
            elif s[i]=="e":
                if state==2 or state==3 or state==8:
                    state=4
                    continue
                else:
                    return False
            else:
                return False
        return state==2 or state==3 or state==5 or state==8

            


s = Solution()
f = s.isNumber(" 0e   ")
print(f)
 