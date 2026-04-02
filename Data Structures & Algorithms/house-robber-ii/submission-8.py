class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            prev, curr = 0, 0

            for n in nums:
                tmp = curr
                curr = max(n + prev, curr)
                prev = tmp
            return curr
        if len(nums) == 1:
            return nums[0]
        
        return max(helper(nums[1:]), helper(nums[:-1]))




