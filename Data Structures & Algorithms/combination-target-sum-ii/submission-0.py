class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return

            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                # if total + candidates[j] > target:
                #     break
                combo.append(candidates[j])
                dfs(j + 1, combo, total + candidates[j])
                combo.pop()

        dfs(0, [], 0)

        return res 