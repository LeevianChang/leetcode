import re
class Solution:

    def addBinary(self, a: str, b: str) -> str:
        maxLength = max(len(a),len(b))
        minLength = min(len(a),len(b))
        resZero = ""
        for i in range(maxLength-minLength):
            resZero+="0"
        if len(a)==minLength:
            a = resZero+a
        else:
            b = resZero+b

        resStr = ""
        extra = 0
        for i in range(maxLength-1,-1,-1):
            current = int(a[i])+int(b[i])+extra
            if extra==0:
                if current==2:
                    resStr="0"+resStr
                    extra = 1
                elif current==1:
                    resStr="1"+resStr
                    extra = 0
                elif current==0:
                    resStr="0"+resStr
                    extra = 0
            else:
                if current==2:
                    resStr="1"+resStr
                    extra = 1
                elif current==1:
                    resStr="0"+resStr
                    extra = 1
                elif current==0:
                    resStr="1"+resStr
                    extra = 0

        if extra==1:
            
            resStr = "1"+resStr
            




        return resStr




s = Solution()
f = s.addBinary("0","0")
print(f)
 