class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()
        rows = len(grid)
        cols = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            seen.add((r, c))
            size = 0

            while q:
                r, c = q.popleft()
                dirs = [[0,1],[0,-1],[1,0],[-1,0]]
                size += 1
                for dr, dc in dirs:
                    row = r + dr
                    col = c + dc
                    if col in range(cols) and row in range(rows) and (row, col) not in seen and grid[row][col] == 1:
                        q.append((row, col))
                        seen.add((row, col))
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    island_size = bfs(r, c)
                    res = max(res, island_size)
        return res