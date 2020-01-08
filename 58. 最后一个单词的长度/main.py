
import collections

class Solution:

    def lengthOfLastWord(self, s):
        s = s.strip()
        string = s.split(" ")
        if len(string)>0:
            return len(string[-1])
        else:
            return 0
        
s = Solution()
f = s.lengthOfLastWord("a   ")
print(f)
