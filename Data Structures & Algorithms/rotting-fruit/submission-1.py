class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        num_healthy_start = 0
        num_infected = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    num_healthy_start += 1
        
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        while q:
            popped_r, popped_c, popped_minutes = q.popleft()
            for dr, dc in dirs:
                new_r, new_c = popped_r + dr, popped_c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        res = max(res, popped_minutes + 1)
                        q.append((new_r, new_c, popped_minutes + 1))
                        num_infected += 1
        
        if num_healthy_start > num_infected:
            return -1
        
        else:
            return res


