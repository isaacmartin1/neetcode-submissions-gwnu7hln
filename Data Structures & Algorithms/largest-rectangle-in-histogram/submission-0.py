class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangles = [] # index, size
        res = 0
        for idx, h in enumerate(heights):
            start_idx = idx
            # while loop only checks condition at top each time in the actual while
            while rectangles and h < rectangles[-1][1]:
                popped_idx, popped_h = rectangles.pop()
                res = max(popped_h * (idx - popped_idx), res)
                start_idx = popped_idx
            rectangles.append([start_idx, h])

        for i, h in rectangles:
            res = max(res, (len(heights) - i) * h)
        return res
