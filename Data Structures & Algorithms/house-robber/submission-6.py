class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0

        for n in nums:
            tmp = curr
            curr = max(n + prev, curr)
            prev = tmp
        
        return curr
