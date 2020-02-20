class Solution:
    dp = []
    def kmp(self, text,pattten) -> int:
        self.build(pattten)
        return self.search(text)
        


    def build(self,patten):
        length = len(patten)
        self.dp = []*length
        for _ in range(length):
            alphabetDict = {}
            for alphabet in range(97,123,1):
                alphabetDict[alphabet] = 0
            self.dp.append(alphabetDict)
        
        
        self.dp[0][ord(patten[0])] = 1
        history = 0
        for i in range(1,length):
            for alphabet in range(97,123,1):
                if ord(patten[i])==alphabet:
                    self.dp[i][alphabet] = i+1
                else:
                    # if dp[history].get(alphabet)!=None:
                    
                    self.dp[i][alphabet] = self.dp[history][alphabet]

            history = self.dp[history][ord(patten[i])]


    def search(self,text):
        end = len(self.dp)
        status = 0
        for i in range(len(text)):
            status = self.dp[status][ord(text[i])]
            if status == end:
                return True

        return False
        
        
s = Solution()


res = s.kmp("abcabababc","abdc")


print(res)
