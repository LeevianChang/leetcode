class Solution:
    def candy(self, ratings) -> int:
        left = [0]*len(ratings)
        right = [0]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        count = left[-1]
        for i in range(len(ratings)-2,-1,-1):
         
            if ratings[i]>ratings[i+1]:
                right[i] = right[i+1]+1
            count +=max(left[i],right[i])
        return count+len(ratings)


        
        
s = Solution()


res = s.candy([1,0,2])

print(res)
