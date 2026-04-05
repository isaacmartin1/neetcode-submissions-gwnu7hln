class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(r):
            if r == 0:
                return 1
            elif r < 0:
                return 0
            
            if r in memo:
                return memo[r]
            
            ways = 0
            for n in nums:
                ways += dfs(r - n)
                    
            memo[r] = ways
            return ways
            
        
        return dfs(target)