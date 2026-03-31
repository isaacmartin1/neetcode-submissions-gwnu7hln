class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # idx, height
        res = 0
        for i, h in enumerate(heights):
            start_idx = i
            while stack and h < stack[-1][1]:
                popped_idx, popped_h = stack.pop()
                res = max(res, popped_h * (i - popped_idx))
                start_idx = popped_idx
            stack.append([start_idx, h])

        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res
