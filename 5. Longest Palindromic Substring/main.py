class Solution:
    def longestPalindrome(self, s):
        # 创建存储回文长度的list,初始长度均为0
        palindromeList = []
        for i in range(len(s)):
           palindromeList.append( 0)
        maxEnd = 0
        maxLength = 1
        length = len(s)
       
        for i in range(length):
            for j in range(length):
                if s[i]==s[j]:
                    if j==length-1:
                        palindromeList[j] = 1
                    else:
                        palindromeList[j] = palindromeList[j+1] +1
                    if j +palindromeList[j]-1==i and palindromeList[j]>maxLength:
                        maxLength = palindromeList[j]
                        maxEnd = j
                else:
                    palindromeList[j] = 0
       
        return s[maxEnd:maxEnd+maxLength]
        





s = Solution()

f = s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")

print(f)