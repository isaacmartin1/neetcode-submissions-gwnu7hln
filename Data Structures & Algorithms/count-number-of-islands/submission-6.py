class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row_n, col_n = len(grid), len(grid[0])

        coordinates = ((1,0),(-1,0),(0,1),(0,-1))


        def dfs(r,c):
            if grid[r][c] == "1":
                grid[r][c] = '#'
            
            for dr, dc in coordinates:
                new_r, new_c = r + dr, c + dc
                if (new_r < 0 or new_r >= row_n or new_c < 0 or new_c >= col_n 
                    or grid[new_r][new_c] == "0" or grid[new_r][new_c] == "#"):
                    continue
                dfs(r + dr, c + dc)

            return 1

        islands = 0

        for r in range(row_n):
            for c in range(col_n):

                if grid[r][c] == '1':
                    islands += dfs(r,c)

        return islands
            
