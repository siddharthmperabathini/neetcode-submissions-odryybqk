class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # go around the border and just DFS on the Os marking all of them safe
        #then mark everything else X
        r = len(board)
        c = len(board[0])
        def dfs(i,j):
            if i == -1 or j == -1 or i == r or j ==c or board[i][j] == 'S' or board[i][j] == 'X':
                return
            board[i][j] = 'S'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(r):
            dfs(i,0)
            dfs(i,c-1)
        for i in range(c):
            dfs(0,i)
            dfs(r-1,i)
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'S':
                    board[i][j] = 'O'

        
