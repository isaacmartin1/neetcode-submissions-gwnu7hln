class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0

        for col in range(len(grid)):
            for row in range(len(grid[0])):
                val = grid[col][row]
                if val == 0:
                    continue
                # check borders
                res += self.num_edges(row, col, grid)

        return res
                
    def num_edges(self, row, col, grid):
        subtotal = 0

        # row up
        if row - 1 < 0:
            subtotal += 1
        elif grid[col][row-1] == 0:
            subtotal += 1

        # row down
        if row + 1 > len(grid[0]) - 1:
            subtotal += 1
        elif grid[col][row+1] == 0:
            subtotal += 1
        
        # col left
        if col - 1 < 0:
            subtotal += 1
        elif grid[col-1][row] == 0:
            subtotal += 1

        # col right
        if col + 1 > len(grid) - 1:
            subtotal += 1
        elif grid[col+1][row] == 0:
            subtotal += 1

        return subtotal








        return subtotal

                