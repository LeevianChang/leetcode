class Solution:

    def isPalindrome(self, s: str) -> bool:
        validIndex = 0
        length = len(s)
        for i in range(length):
            if s[i].isdigit() or s[i].isalpha():
                validIndex+=1
                while s[length-validIndex].isdigit()==False and s[length-validIndex].isalpha()==False:
                    validIndex+=1
                if s[length-validIndex].lower()!=s[i].lower():
                    return False
                

        
        return True
        
        
s = Solution()


res = s.isPalindrome("")
print(res)

 