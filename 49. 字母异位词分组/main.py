
class Solution:
    def groupAnagrams(self, strs):
        mapStrs = {}
        for i in range(len(strs)):
            sortedStrs = tuple(sorted(strs[i]))
            if mapStrs.get(sortedStrs)==None:
                mapStrs[sortedStrs] = []
            mapStrs[sortedStrs].append(strs[i])
        res = []
        for i in mapStrs:
            res.append(mapStrs[i])
        return res
        
        


            
s = Solution()
f = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(f)
