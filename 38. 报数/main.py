class Solution:
    def countAndSay(self, n):
        if n==1:
            return "1"
        last = self.countAndSay(n-1)
        this = ""
        count = 1
        for i in range(0,len(last)):
      
            if i+1<=len(last)-1 and last[i]==last[i+1]:
                count+=1
            else:
                # print(count)
                this +=str(count)+last[i]
                count = 1
        # print(this)
        return this

            




    

s = Solution()
f = s.countAndSay(5)
print(f)
