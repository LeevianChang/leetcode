class Solution:
    def lengthOfLongestSubstring(self, s):
        stringMap = {}
        start = 0
        end = 0
        res = 0
        for i in range(len(s)):
            end = i+1
            # print(s[i],stringMap.get(s[i]))
            if stringMap.get(s[i])==None:
                stringMap[s[i]]=True
            else:

                while s[start]!=s[i]:
                    stringMap[s[start]]=None

                    start+=1
                start+=1
            res = max(res,end-start)
            # print(s[start:end],res)

        return res

    



s = Solution()

f = s.lengthOfLongestSubstring("abb")

print(f)