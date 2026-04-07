class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return False
            
            if word[i] != board[r][c]:
                return False
            
            if board[r][c] == '#':
                return False

            board[r][c] = '#'

            new_i = i + 1
            res = (
                dfs(r + 1, c, new_i) or
                dfs(r - 1, c, new_i) or
                dfs(r, c + 1, new_i) or
                dfs(r, c - 1, new_i)
            )

            board[r][c] = word[i]

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r, c, 0):
                    return True

        return False