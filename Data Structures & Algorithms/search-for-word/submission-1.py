class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(coord, board, word_pos, word):
            if word_pos == len(word):
                return True
            row, col = coord
            board[row][col] = "#"
            if col + 1 < len(board[0]) and board[row][col+1] == word[word_pos]:
                if dfs((row, col + 1), board, word_pos + 1, word):
                    return True
            if col - 1 >= 0 and board[row][col-1] == word[word_pos]:
                if dfs((row, col - 1), board, word_pos + 1, word):
                    return True
            if row + 1 < len(board) and board[row + 1][col] == word[word_pos]:
                if dfs((row + 1, col), board, word_pos + 1, word):
                    return True
            if row - 1 >= 0 and board[row - 1][col] == word[word_pos]:
                if dfs((row - 1, col), board, word_pos + 1, word):
                    return True
            board[row][col] = word[word_pos - 1]

            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and (dfs((r,c), board, 1, word)):
                    return True
        return False

