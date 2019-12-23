class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        res = []
        windowLenght = len(words)
        if windowLenght==0:
            return []
        wordsLen = len(words[0])
       
        wordsC = Counter(words)
        for i in range(len(s)-len(words) * wordsLen+1):
            sMap = []
            for j in range(i,i+windowLenght*wordsLen,wordsLen):
                end =j+wordsLen
                sMap.append(s[j:end])
            
            if Counter(sMap) == wordsC:
                res.append(i)
              

        return res

    def findSubstring2(self, s, words):
        
        from collections import Counter
        # 窗口长度
        wLen = len(words)
        if wLen==0:
            return []
        res = set()
        wordsLen = len(words[0])
        # ist 转hashMap
        words = Counter(words)
        
        # i循环一个单词的长度
        for i in range(0, wordsLen):
            # 窗口起始点
            start = i
            # 窗口结束点
            end = i
            # 记录本次遍历一个单词长度出现的个数
            curCounter = Counter()
            # 窗口中的单词个数
            curWords= 0

            # 结束点不能超过字符串长度
            while end+wordsLen<=len(s):
                
                thisWord = s[end:end+wordsLen]
                end = end+wordsLen
                # 单词出现的字数记录+1
                curCounter[thisWord]+=1
                # 当前窗口中出现的单词个数+1
                curWords +=1
                # 当前单词出现的次数超过了words中单词出现的次数
                while curCounter[thisWord]>words[thisWord]:
                    # 从开头开始减，直到减掉超过的那个词，循环会退出
                    curCounter[s[start:start+wordsLen]]-=1
                    start = start+wordsLen
                    curWords -=1
                # 如果窗口中的单词个数与需求的一致
                if  curWords==wLen:
                    res.add(start)
        return list(res)







            

                     
            


    

s = Solution()
f = s.findSubstring2("mississippi",["is"])


print(f)