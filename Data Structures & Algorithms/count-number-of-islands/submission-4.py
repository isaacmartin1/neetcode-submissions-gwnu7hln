from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def bfs(row, col):
            visited.add((row, col))
            queue = deque([(row, col)])
            print('new search')
            while queue:
                row, col = queue.popleft()
                for x_dir, y_dir in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                    new_row, new_col = row + y_dir, col + x_dir
                    if new_row < 0 or new_col < 0 or new_row >= len(grid) or new_col >= len(grid[0]):
                        continue

                    if grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        print('connection added')
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        visited = set()
        for row in range(len(grid)):
            print("visited:", visited)
            for col in range(len(grid[0])):
                if (row, col) in visited or grid[row][col] == "0":
                    continue
                bfs(row, col)
                res += 1
        
        return res