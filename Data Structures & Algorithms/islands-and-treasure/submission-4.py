class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        self.inf = 2 ** 31 - 1
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c, 1))
        
        while q:
            popped_r, popped_c, popped_dist = q.popleft()
            dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            for dr, dc in dirs:
                new_r, new_c = popped_r + dr, popped_c + dc
                if new_r in range(rows) and new_c in range(cols):
                    if grid[new_r][new_c] == self.inf:
                        grid[new_r][new_c] = popped_dist
                        q.append((new_r, new_c, popped_dist + 1))
    