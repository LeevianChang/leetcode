import re
class Solution:

    def plusOne(self, digits):
        extra = 0
        for i in range(len(digits)-1,-1,-1):
            if i==(len(digits)-1):

                add = digits[i]+1
                if add>=10:
                    extra = 1
                    digits[i] = add-10
                else:
                    extra=0
                    digits[i] = add
            else:
                if extra==1:
                    add = digits[i]+1
                    if add>=10:
                        extra = 1
                        digits[i] = add-10
                    else:
                        extra=0
                        digits[i] = add

                else:
                    break
        if extra==1:
            digits.insert(0,1)
        return digits


s = Solution()
f = s.plusOne([9,9,9])
print(f)
 