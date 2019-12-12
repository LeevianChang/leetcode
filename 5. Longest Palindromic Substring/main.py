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

    # 动态规划解法
    def longestPalindromeDP(self, s):
        # 记录子字符串是否是回文
        subsetArr = []
        for i in range(len(s)-1):
            
            subsetArr.append([0]*len(s))
        start = 0 
        maxLength = 1
        for i in range(len(s)-1,-1,-1):
            for j in range(len(s)-1,i,-1):
                if i==len(s):
                    subsetArr[i][j] = 0
                if i==j:
                    subsetArr[i][j] = 1
    
                if s[i]!=s[j]:
                    subsetArr[i][j]=0
                    continue
                if i+1==j and s[i]==s[j]:
                    subsetArr[i][j] = 2
                if i+2==j and s[i]==s[j]:
                    subsetArr[i][j] = 3
                if j>i+2 and s[i]==s[j] and subsetArr[i+1][j-1]>0:
                    subsetArr[i][j] = subsetArr[i+1][j-1]+2
                if subsetArr[i][j]>maxLength:
                    maxLength = subsetArr[i][j]
                    start  = i

        return s[start:start+maxLength]
                
        

       




s = Solution()

# f = s.longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")
f = s.longestPalindromeDP("abcdfcba")
print(f)