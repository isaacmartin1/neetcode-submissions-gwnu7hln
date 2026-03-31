class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        seen = set()
        rows, cols = len(grid), len(grid[0])
        total = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            seen.add((r, c))

            while q:
                r, c = q.popleft()

                directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if new_row in range(rows) and new_col in range(cols) and grid[r][c] == '1' and (new_row, new_col) not in seen:
                        q.append((new_row, new_col))
                        seen.add((new_row, new_col))
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in seen:
                    bfs(r, c)
                    total += 1
        
        return total