class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # idx, temp

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, popped_i = stack.pop()
                res[popped_i] = i - popped_i
            stack.append([t, i])
        return res