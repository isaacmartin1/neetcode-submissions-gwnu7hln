class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangle = []
        res = 0

        for i, h in enumerate(heights):
            start_idx = i
            while rectangle and h < rectangle[-1][1]:
                popped_idx, popped_h = rectangle.pop()
                res = max(res, popped_h * (i - popped_idx))
                start_idx = popped_idx
            rectangle.append([start_idx, h])
        
        for i, h in rectangle:
            res = max(res, h * (len(heights) - i))
        
        return res