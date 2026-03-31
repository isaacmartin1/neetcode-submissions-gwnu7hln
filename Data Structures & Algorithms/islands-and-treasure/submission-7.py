class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.inf = 2 ** 31 - 1
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            popped_r, popped_c = q.popleft()
            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                new_r, new_c = popped_r + dr, popped_c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] == self.inf:
                        grid[new_r][new_c] = grid[popped_r][popped_c] + 1
                        q.append((new_r, new_c))
    