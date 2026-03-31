class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        self.inf = 2**31 - 1
        rows, cols = len(grid), len(grid[0])


        def bfs(r, c, dist):
            q = collections.deque()
            seen = set()
            seen.add((r, c))
            q.append((r, c, dist, seen))            

            while q:
                popped_r, popped_c, popped_dist, popped_seen = q.popleft()
                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in dirs:
                    new_r, new_c = popped_r + dr, popped_c + dc
                    if new_r in range(rows) and new_c in range(cols) and (new_r, new_c) not in popped_seen:
                        if grid[new_r][new_c] == 0:
                            return popped_dist
                        elif grid[new_r][new_c] != 0 and grid[new_r][new_c] != -1:
                            popped_seen.add((new_r, new_c))
                            q.append((new_r, new_c, popped_dist + 1, popped_seen))
            return self.inf

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == self.inf:
                    grid[r][c] = bfs(r, c, 1)

