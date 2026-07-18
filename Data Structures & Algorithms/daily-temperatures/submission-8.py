class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = [0 for _ in range(len(temperatures))]
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, popped_i = stack.pop(-1)
                temps[popped_i] = i - popped_i

            stack.append([t, i])



        return temps