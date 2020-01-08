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


    def longestPalindromeDP(self, s):
        start = 0
        maxLength = 1
        length = len(s)
        a = []
        for i in range(length):
            a.append([0]*length)

        for j in range(length):
            for i in range(j,-1,-1):
                if s[j]==s[i]:
                    if j==i+1:
                        a[i][j] = 2
                    if j==i+2:
                        a[i][j] = 3
                    if j>i+2 and a[i+1][j-1]>0:
                        a[i][j] = a[i+1][j-1]+2

                    if a[i][j]>maxLength:
                        maxLength = a[i][j]
                        start = i
        return s[start:start+maxLength]


        


                    
s = Solution()

# f = s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
f = s.longestPalindromeDP("abacab")
print(f)