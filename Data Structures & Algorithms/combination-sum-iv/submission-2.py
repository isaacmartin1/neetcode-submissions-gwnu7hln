from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Dictionary to store the results of already computed subproblems
        memo = {}

        def dfs(r):
            # Base cases
            if r == 0:
                return 1
            if r < 0:
                return 0
            
            # If we have already calculated the result for this remaining target, return it
            if r in memo:
                return memo[r]

            # Calculate the number of combinations for the current remaining target
            ways = 0
            for n in nums:
                ways += dfs(r - n)

            # Cache the result before returning
            memo[r] = ways
            return ways

        return dfs(target)