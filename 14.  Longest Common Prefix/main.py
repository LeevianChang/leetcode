class Solution:
    # 使用分治的思想
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        return self.commonPrefix(strs,0,len(strs)-1)

    def commonPrefix(self,strs,i,j):
        if i==j:
            return strs[i]
        mid = int((j+i)/2)

        l = self.commonPrefix(strs,i,mid)
        r = self.commonPrefix(strs,mid+1,j)
        return self.getCommonPrefix(strs,l,r)

    def getCommonPrefix(self,strs,left,right):
    
        minLength = len(left)
        if len(right)<minLength:
            minLength = len(right)
        for i in range(minLength):
           
            if left[i]==right[i]:
                if i==minLength-1:
                    return left[0:i+1]
            else:
                return left[0:i]
        return ""



s = Solution()

f = s.longestCommonPrefix(["leetcode","leet","lee","le"])

print(f)