
digitsList = [
            " ",
            " ",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "qprs",
            "tuv",
            "wxyz",
]
class Solution:
    def letterCombinations(self, digits):
        resList = []

        if digits=="":
            return resList
        self.getLetterCombination(digits,0,"",resList)
        return resList

    def getLetterCombination(self,digits,index,temp,res):
        # 当前的索引已经是最后一个数字了
        if index==len(digits):
            res.append(temp)
            return 
        # 获取当前的数字
        num= int(digits[index])
        for i in digitsList[num]:
            self.getLetterCombination(digits,index+1,temp+i,res)





s = Solution()

f = s.letterCombinations("")

print(f)