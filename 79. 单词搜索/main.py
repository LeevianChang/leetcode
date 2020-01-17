class Solution:
    resBool = False
    def exist(self, board, word) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            
            for j in range(n):

                if board[i][j]==word[0]:
                    visited[i][j] = 1
                    res = self.existHelper(board,i,j,word[1:],visited)
                    if res==True:
                        return True

                    visited[i][j] = 0
                    
                   
        return self.resBool
    
    def existHelper(self,board,i,j,word,visited):


        if len(word)==0:
            return True
        
        direction =[(0,1),(0,-1),(-1,0),(1,0)]
        for k in range(len(direction)):
            newI = i+direction[k][0]
            newJ = j+direction[k][1]
            # print(i,j,newI,newJ)
            if newI<len(board) and newI>=0 and newJ<len(board[0]) and newJ>=0 and board[newI][newJ]==word[0] and visited[newI][newJ]==0:
                visited[newI][newJ] = 1
                res = self.existHelper(board,newI,newJ,word[1:],visited)
                visited[newI][newJ] = 0
                # 最开始做的时候，没有在这里加上判断，导致会超时，原因在于题目只需要找到一个正确的答案即可，不需要找到所有的
                if res==True:
                    return True



            


s = Solution()
board = [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ["a","b"],
# ["c","d"]
    # ["C","A","A"],
    # ["A","A","A"],
    # ["B","C","D"]
    ["a"],["a"]
]

f = s.exist(board,"aaa")
print(f)
 