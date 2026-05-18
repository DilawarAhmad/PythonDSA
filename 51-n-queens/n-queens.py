class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        ans = []
        self.nQueens(board,n,0,ans)
        return ans

    def nQueens(self,board,n,row,ans):
        if row == n:
            temp = ["".join(r) for r in board]
            ans.append(temp)
            return 

        for j in range(n):
            if self.isSafe(board,n,row,j):
                board[row][j] = "Q"
                self.nQueens(board,n,row+1,ans)
                board[row][j] = "."
    def isSafe(self,board,n,row,col):
        #row check
        for i in range(n):
            if board[row][i]=="Q":
                return False
        # cols check
        for i in range(n):
            if board[i][col]=="Q":
                return False
        # left diagonal check 
        for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
            if board[i][j]=="Q":
                return False
        #right diagonal check 
        for i, j in zip(range(row,-1,-1) , range(col,n)):
            if board[i][j]=="Q":
                return False
        return True



