class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, combo):
            if sum(combo) == target:
                self.res.append(combo.copy())
                return
            if sum(combo) > target or i == len(nums):
                return

            combo.append(nums[i])
            dfs(i, combo)
            combo.pop()
            dfs(i + 1, combo)

        dfs(0, [])
        return self.res
