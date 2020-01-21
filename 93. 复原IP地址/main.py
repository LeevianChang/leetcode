class Solution:
   


    def restoreIpAddresses(self, s: str):
        
        resList = []
        self.restoreIpAddressesHelper(s,[],resList)
        return resList


    def restoreIpAddressesHelper(self,s,current,resList):
        if len(current)==4:
            if len(s)==0:
                resList.append('.'.join(current))
            else:
                return 
        for k in range(1,4):
                if k > len(s):
                    break
                if k>1 and s[0]=="0":
                    continue 
                if int(s[:k])<=255:
                    self.restoreIpAddressesHelper(s[k:],current+[s[:k]],resList)



       
    



s = Solution()

f = s.restoreIpAddresses("010010")
print(f)
 