class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        rows, cols = len(heights), len(heights[0])
        def dfs(r, c, target_set):
            target_set.add((r, c))
            curr_val = heights[r][c]
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc
                
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in target_set:
                    new_val = heights[new_r][new_c]
                    if new_val >= curr_val:    
                        dfs(new_r, new_c, target_set)
            return target_set

        # bottom
        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        
        # right
        for r in range(rows):
            att_to_atl = dfs(r, cols - 1, atlantic)
    
        # top
        for c in range(cols):
            dfs(0, c, pacific)

        # left
        for r in range(rows):
            dfs(r, 0, pacific)

        
        res = []
        for a in atlantic:
            if a in pacific:
                r, c = a
                res.append([r, c])
        
        return res