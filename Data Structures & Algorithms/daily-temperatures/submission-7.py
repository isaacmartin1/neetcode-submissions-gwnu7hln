class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # t, i

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, stack_idx = stack.pop()
                res[stack_idx] = i - stack_idx
            stack.append([t, i])


        return res