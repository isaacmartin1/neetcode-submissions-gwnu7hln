class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            # check 4 around
            if r < 0 or r >= len(board):
                return False
            
            if c < 0 or c >= len(board[0]):
                return False
            
            if board[r][c] == '#':
                return False
            
            if word[i] != board[r][c]:
                return False
            
            board[r][c] = '#'

            res = (dfs(r - 1, c, i + 1) or
                dfs(r + 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            
            board[r][c] = word[i]
            return res



        for c in range(len(board[0])):
            for r in range(len(board)):
                if dfs(r, c, 0):
                    return True

        return False    