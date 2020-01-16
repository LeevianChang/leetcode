class Solution:
    
    def isMatch(self,sMap,tMap):
        # print(sMap,tMap)
        for i in tMap:
            if sMap.get(i)==None:
                return False
            if sMap[i]<tMap[i]:
                return False
            
        return True

         


    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for i in range(len(t)):
            if tMap.get(t[i])==None:
                tMap[t[i]] = 1
            else:
                tMap[t[i]] += 1
        i = 0
        j = 0
        isTrue = False
        start = 0
        end = len(s)
        sMap = {}
        while i<=len(s)-1 and j<len(s)+1:
            
            if len(sMap)>=len(tMap) and self.isMatch(sMap,tMap):
                if j-i<end-start:
                    start = i
                    end = j
                sMap[s[i]]-=1
                isTrue = True
                i+=1
            else:
                if j<=len(s)-1:
                    if sMap.get(s[j])!=None:
                        sMap[s[j]] +=1
                    else:
                        sMap[s[j]] = 1
            
                j+=1
                    
                
                
        

        if isTrue==True:
            return s[start:end]
        else:
            return ""

    

    def minWindow3(self, s: 'str', t: 'str') -> 'str':

        tMap = {}
        for i in range(len(t)):
            if tMap.get(t[i])==None:
                tMap[t[i]] = 1
            else:
                tMap[t[i]] += 1
        start = 0
        end = len(s)-1
        i = 0
        j = 0
        res = ""
        count = len(t)
        while j<len(s):
            if tMap.get(s[j])!=None:
                tMap[s[j]]-=1
            if  tMap.get(s[j])!=None and tMap[s[j]]>=0:
                count-=1
            while count==0:
                if j-i<=end-start:
                    res = s[i:j+1]
                    end = j
                    start = i
                if tMap.get(s[i])!=None:
                    tMap[s[i]]+=1
                if tMap.get(s[i])!=None and tMap[s[i]]>0:
                    count+=1
                i+=1
            j+=1

        return res



    def minWindow2(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res
        
    

s = Solution()
f = s.minWindow3("a","a")
print(f)
 