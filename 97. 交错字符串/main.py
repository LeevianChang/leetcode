class Solution:
   


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1+n2!=n3:
            return False
        return self.isInterleaveHelper(s1,s2,s3)
        
    def isInterleaveHelper(self,s1,s2,s3):
        if len(s3)==0:
            return True
        if len(s1)>0 and s1[0]!=s3[0] and len(s2)>0 and s2[0]!=s3[0]:
            return False

        r1 = r2 = False
        if len(s1)>0 and s1[0]==s3[0]:
            r1 = self.isInterleaveHelper(s1[1:],s2,s3[1:])

        if len(s2)>0 and s2[0]==s3[0]:
            r2 =  self.isInterleaveHelper(s1,s2[1:],s3[1:])
        
         
        return r1 or r2

    
       
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        
        l3 = len(s3)
        if l1+l2!=l3:
            return False
        s3 = " "+s3
        dpList = []*(l2+1)
        for i in range(l2+1):
            dpList.append([False]*(l1+1))

        for i in range(l2+1):
            for j in range(l1+1):
                if i==0 and j==0:
                    dpList[i][j] = True
                    continue

                if i ==0 and j>0:
                    dpList[i][j] = dpList[i][j-1] and s1[j-1]==s3[j]
                    continue
                if j==0 and i>0:
                    dpList[i][j] = dpList[i-1][j] and s2[i-1]==s3[i]
                    continue

                dpList[i][j] = (dpList[i-1][j] and s2[i-1]==s3[i+j]) or (dpList[i][j-1] and s1[j-1]==s3[i+j])
        return dpList[-1][-1]





s = Solution()

f = s.isInterleave2("","","a")
print(f)
 